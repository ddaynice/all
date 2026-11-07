/* 面试自测 · 写答案 + AI 判卷 + 间隔重复 */
(function () {
  'use strict';

  var STORE_KEY = 'interview-quiz-progress-v1';
  var OVERRIDE_KEY = 'interview-quiz-overrides-v1';
  var AI_KEY = 'interview-quiz-ai-v1';
  var THEME_KEY = 'interview-quiz-theme';
  var INTERVALS = [0, 1, 2, 4, 7, 15]; // Box 0..5 对应的间隔天数
  var DAY = 86400000;

  var DATA = window.QUIZ_DATA || { categories: [], types: [], questions: [], generatedAt: '' };
  var RAW = DATA.questions || [];
  var progress = load(STORE_KEY, {});
  var overrides = load(OVERRIDE_KEY, {});
  var aiConf = load(AI_KEY, { base: '', key: '', model: '' });

  var state = {
    mode: 'review',
    category: '',
    dueOnly: true,
    queue: [],
    cursor: 0,
    current: null,
    revealed: false,
    judging: false,
    chat: [] // 追问对话 [{role:'assistant'|'user', content}]
  };

  var $ = function (id) { return document.getElementById(id); };

  // ---------------- 存储 ----------------
  function load(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) { return fallback; }
  }
  function save(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) { /* 忽略 */ }
  }
  function recOf(id) {
    if (!progress[id]) progress[id] = { box: 0, due: 0, seen: 0, hit: 0 };
    return progress[id];
  }
  function cardOf(item) {
    var ov = overrides[item.id];
    return ov ? {
      id: item.id, category: item.category, type: item.type, source: item.source,
      question: ov.question || item.question, answer: ov.answer || item.answer
    } : item;
  }

  // ---------------- 渲染 ----------------
  function renderMD(text) {
    if (!text) return '';
    var s = String(text).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    s = s.replace(/```[\w]*\n?([\s\S]*?)```/g, function (m, code) {
      return '<pre><code>' + code.replace(/\n$/, '') + '</code></pre>';
    });
    s = s.replace(/`([^`\n]+)`/g, '<code>$1</code>');
    s = s.replace(/^#{1,6}\s+(.+)$/gm, '<h4>$1</h4>');
    s = s.replace(/^\s*[-*+]\s+(.+)$/gm, '<li>$1</li>');
    s = s.replace(/(?:<li>[\s\S]*?<\/li>\n?)+/g, function (m) {
      return '<ul>' + m.replace(/\n/g, '') + '</ul>';
    });
    s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/\n{2,}/g, '</p><p>');
    s = s.replace(/\n/g, '<br>');
    return '<p>' + s + '</p>';
  }
  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
  }

  function refreshMeta() {
    var line = $('meta-line');
    if (!RAW.length) {
      line.textContent = '题库为空 · 先跑 tools/import_feishu.py';
      return;
    }
    var scope = state.category ? RAW.filter(function (q) { return q.category === state.category; }) : RAW;
    line.textContent = RAW.length + ' 题 · 待复习 ' + dueCount(scope) + ' · 生成于 ' + (DATA.generatedAt || '-');
  }

  function dueCount(list) {
    var now = Date.now(), n = 0;
    list.forEach(function (it) { if (recOf(it.id).due <= now) n++; });
    return n;
  }

  function initFilters() {
    var cats = (DATA.categories && DATA.categories.length)
      ? DATA.categories.slice()
      : Array.from(new Set(RAW.map(function (q) { return q.category; })));
    [$('cat-filter'), $('cat-filter2')].forEach(function (sel) {
      sel.innerHTML = '<option value="">全部分类</option>' +
        cats.map(function (c) {
          return '<option value="' + esc(c) + '">' + esc(c) + '（' +
            RAW.filter(function (q) { return q.category === c; }).length + '）</option>';
        }).join('');
    });
  }

  // ---------------- 队列 ----------------
  function buildQueue() {
    var now = Date.now();
    var pool = RAW.filter(function (q) {
      if (state.category && q.category !== state.category) return false;
      if (state.dueOnly && recOf(q.id).due > now) return false;
      return true;
    });
    shuffle(pool);
    pool.sort(function (a, b) {
      var ra = recOf(a.id), rb = recOf(b.id);
      return (ra.box - rb.box) || (ra.due - rb.due);
    });
    state.queue = pool;
    state.cursor = 0;
    $('queue-info').textContent = pool.length ? ('本轮 ' + pool.length + ' 题') : '本轮 0 题';
    nextCard();
  }
  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
  }

  function nextCard() {
    var card = $('quiz-card'), empty = $('review-empty');
    if (state.cursor >= state.queue.length) {
      state.current = null;
      card.classList.add('hidden');
      empty.classList.remove('hidden');
      $('queue-info').textContent = '本轮已完成';
      return;
    }
    empty.classList.add('hidden');
    card.classList.remove('hidden');

    var item = state.queue[state.cursor];
    state.current = item;
    state.revealed = false;
    state.judging = false;

    var rec = recOf(item.id);
    $('c-category').textContent = item.category || '其他';
    $('c-type').textContent = item.type || '理论';
    $('c-box').textContent = 'Box ' + rec.box + ' · 见过 ' + rec.seen + ' 次';
    $('c-source').textContent = item.source || '';
    $('c-question').textContent = cardOf(item).question;

    $('c-answer').innerHTML = renderMD(cardOf(item).answer);
    $('c-answer').classList.add('hidden');
    $('verdict-box').classList.add('hidden');
    $('verdict-box').innerHTML = '';
    $('answer-input').value = '';
    $('input-wrap').classList.remove('hidden');
    $('btn-ai').classList.remove('hidden');
    $('btn-show').classList.remove('hidden');
    $('grade-box').classList.add('hidden');
    $('btn-show').textContent = '直接看答案 (空格)';

    state.chat = [];
    $('chat-box').innerHTML = '';
    $('chat-box').classList.add('hidden');
    $('chat-input-wrap').classList.add('hidden');
    $('chat-input').value = '';

    $('queue-info').textContent = (state.cursor + 1) + ' / ' + state.queue.length;
  }

  function reveal() {
    if (!state.current) return;
    state.revealed = true;
    $('c-answer').classList.remove('hidden');
    $('input-wrap').classList.add('hidden');
    $('btn-ai').classList.add('hidden');
    $('btn-show').classList.add('hidden');
    $('grade-box').classList.remove('hidden');
  }

  function grade(level) {
    if (!state.current) return;
    var rec = recOf(state.current.id);
    rec.seen++;
    if (level === 0) { rec.box = 0; }
    else if (level === 1) { rec.box = Math.max(0, Math.min(rec.box, 2)); }
    else { rec.box = Math.min(5, rec.box + 1); rec.hit++; }
    rec.due = Date.now() + INTERVALS[rec.box] * DAY;
    if (rec.box === 0) rec.due = Date.now();
    save(STORE_KEY, progress);
    state.cursor++;
    refreshMeta();
    nextCard();
  }

  // ---------------- AI 判卷 ----------------
  function openAiModal() {
    $('ai-base').value = aiConf.base || '';
    $('ai-key').value = aiConf.key || '';
    $('ai-model').value = aiConf.model || '';
    $('ai-modal').classList.remove('hidden');
  }
  function closeAiModal() { $('ai-modal').classList.add('hidden'); }

  function extractJson(text) {
    var m = text.match(/\{[\s\S]*\}/);
    if (!m) return null;
    try { return JSON.parse(m[0]); } catch (e) { return null; }
  }

  function chatComplete(messages) {
    var url = aiConf.base.replace(/\/+$/, '') + '/chat/completions';
    return fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + aiConf.key },
      body: JSON.stringify({ model: aiConf.model, temperature: 0.4, messages: messages })
    }).then(function (r) {
      if (!r.ok) return r.text().then(function (t) { throw new Error('HTTP ' + r.status + ' ' + t.slice(0, 200)); });
      return r.json();
    }).then(function (data) {
      var content = data.choices && data.choices[0] && data.choices[0].message
        ? data.choices[0].message.content : '';
      if (!content) throw new Error('AI 返回为空');
      return content;
    });
  }

  function aiReady() {
    if (!aiConf.base || !aiConf.key || !aiConf.model) {
      openAiModal();
      toast('先配置 AI 接口，再开始判卷');
      return false;
    }
    return true;
  }

  function judge() {
    if (!state.current) return;
    if (!aiReady()) return;
    var mine = $('answer-input').value.trim();
    if (!mine) { toast('先写点答案，或者点「直接看答案」'); return; }

    state.judging = true;
    var box = $('verdict-box');
    box.classList.remove('hidden');
    box.innerHTML = '<div class="judging">AI 面试官正在批卷…</div>';

    var sys = '你是严格的大数据方向技术面试官。给你面试题、参考答案和候选人回答。' +
      '对比参考答案评估候选人回答，只输出 JSON，不要任何多余文字：' +
      '{"score": 0-10的整数, "verdict": "掌握|部分|不会", ' +
      '"comment": "两三句话：答对了哪些要点、漏了哪些、有什么明显错误"}。' +
      '评分标准：8-10 掌握（核心要点基本齐全）；4-7 部分（方向对但有遗漏或小错）；0-3 不会（空白、跑题或明显错误）。';
    var user = '【面试题】\n' + cardOf(state.current).question +
      '\n\n【参考答案】\n' + cardOf(state.current).answer +
      '\n\n【候选人回答】\n' + mine;

    state.chat = [{ role: 'user', content: user }];
    chatComplete([{ role: 'system', content: sys }].concat(state.chat))
      .then(function (text) {
        var v = extractJson(text);
        if (!v) throw new Error('AI 返回无法解析：' + text.slice(0, 200));
        state.chat = []; // 对话区从追问开始，判卷消息不进 chat 历史
        state.judging = false;
        v.mine = mine;
        showVerdict(v);
      })
      .catch(function (e) {
        state.judging = false;
        box.innerHTML = '<div class="v-comment">判卷失败：' + esc(String(e.message || e)) +
          '<br><span style="font-size:12px;color:var(--muted)">如果提示 CORS/网络错误，说明该接口不允许浏览器直连，可以换 DeepSeek/智谱等支持 CORS 的服务商，或者告诉我加个本地代理。</span></div>';
      });
  }

  var INTERVIEWER_SYS = '你是一位真实的大数据方向技术面试官，正在对候选人进行模拟面试。规则：' +
    '1) 每轮先用一两句话点评候选人上一段回答（认可或指出问题）；' +
    '2) 然后提出恰好一个更深入的追问，顺着候选人的回答往下挖：底层原理、真实场景、参数调优、方案对比、异常与踩坑；' +
    '3) 用口语化中文自然提问，像真人面试官聊天，绝不要念文档标题；' +
    '4) 候选人答不上来时给一点提示降低难度，而不是直接公布答案；' +
    '5) 输出格式：点评一两句，换行，然后以「追问：」开头的问题。不要输出别的标签。';

  function buildInterviewMessages() {
    var c = cardOf(state.current);
    var first = '【本题考点】\n' + c.question +
      '\n\n【候选人已写下的初步回答】\n' + (state._firstAnswer || '（没写）') +
      '\n\n【参考答案（仅供你参考，不要直接念给候选人）】\n' + c.answer +
      '\n\n请点评他的回答，并抛出第一个追问。';
    var msgs = [{ role: 'system', content: INTERVIEWER_SYS }, { role: 'user', content: first }];
    state.chat.forEach(function (m) {
      msgs.push({ role: m.role, content: m.content });
    });
    return msgs;
  }

  function renderChat() {
    var box = $('chat-box');
    box.classList.remove('hidden');
    box.innerHTML = state.chat.map(function (m) {
      if (m.role === 'user') {
        return '<div class="bubble me">' + esc(m.content) + '</div>';
      }
      return '<div class="bubble interviewer">' +
        esc(m.content).replace(/^(追问[:：])/, '<span class="q-mark">追问</span>') + '</div>';
    }).join('');
    box.scrollTop = box.scrollHeight;
  }

  function followUp(extraUserMsg) {
    if (!state.current) return;
    if (!aiReady()) return;
    if (extraUserMsg) state.chat.push({ role: 'user', content: extraUserMsg });
    renderChat();
    // 打字中占位
    var typing = document.createElement('div');
    typing.className = 'bubble interviewer typing';
    typing.textContent = '面试官思考中…';
    $('chat-box').appendChild(typing);
    $('chat-box').scrollTop = $('chat-box').scrollHeight;

    chatComplete(buildInterviewMessages()).then(function (text) {
      state.chat.push({ role: 'assistant', content: text });
      renderChat();
    }).catch(function (e) {
      typing.textContent = '追问失败：' + String(e.message || e);
    });
  }

  function showVerdict(v) {
    var box = $('verdict-box');
    var score = Math.max(0, Math.min(10, Number(v.score) || 0));
    var verdict = ['掌握', '部分', '不会'].indexOf(v.verdict) >= 0 ? v.verdict : (score >= 8 ? '掌握' : score >= 4 ? '部分' : '不会');
    var cls = verdict === '掌握' ? 'g' : verdict === '部分' ? 'w' : 'b';
    box.innerHTML =
      '<span class="v-score">' + score + '<span style="font-size:12px;color:var(--muted)">/10</span></span>' +
      '<span class="v-tag ' + cls + '">' + verdict + '</span>' +
      '<span class="v-suggest">按 AI 建议记分，或自己改判 ↓</span>' +
      '<div class="v-comment">' + esc(v.comment || '') + '</div>';

    reveal(); // 展开标准答案 + 评分按钮
    var suggest = verdict === '掌握' ? $('btn-good') : verdict === '部分' ? $('btn-hard') : $('btn-again');
    suggest.style.outline = '2px solid var(--brand)';
    suggest.style.outlineOffset = '2px';

    // 进入追问模式
    $('chat-input-wrap').classList.remove('hidden');
    state._firstAnswer = v.mine || '';
    followUp();
  }

  function sendChat() {
    if (!state.current) return;
    var t = $('chat-input').value.trim();
    if (!t) { toast('先写点回答'); return; }
    $('chat-input').value = '';
    followUp(t);
  }

  // ---------------- 浏览 ----------------
  function renderList() {
    var kw = $('search').value.trim().toLowerCase();
    var cat = $('cat-filter2').value;
    var list = RAW.filter(function (q) {
      if (cat && q.category !== cat) return false;
      if (!kw) return true;
      var c = cardOf(q);
      return (c.question + ' ' + c.answer).toLowerCase().indexOf(kw) >= 0;
    });
    $('browse-count').textContent = list.length + ' 题';
    $('list').innerHTML = list.slice(0, 300).map(function (q) {
      var c = cardOf(q);
      return '<div class="item" data-id="' + q.id + '">' +
        '<div class="row"><span class="tag">' + esc(c.category) + '</span>' +
        '<span class="tag ghost">' + esc(c.type || '') + '</span>' +
        '<span class="q">' + esc(c.question) + '</span></div>' +
        '<div class="a collapsed">' + esc(c.answer) + '</div></div>';
    }).join('') || '<div class="empty"><h3>没有匹配的题目</h3></div>';
  }

  // ---------------- 统计 ----------------
  function renderStats() {
    if (!RAW.length) return;
    var now = Date.now();
    var mastered = 0, due = 0, untouched = 0;
    RAW.forEach(function (q) {
      var r = recOf(q.id);
      if (r.box >= 4) mastered++;
      if (r.due <= now) due++;
      if (!r.seen) untouched++;
    });
    $('kpis').innerHTML = [
      ['题库总量', RAW.length],
      ['待复习', due],
      ['已掌握', mastered],
      ['未见过', untouched],
      ['掌握率', Math.round(mastered / RAW.length * 100) + '%']
    ].map(function (p) {
      return '<div class="kpi"><div class="n">' + p[1] + '</div><div class="l">' + p[0] + '</div></div>';
    }).join('');

    var cats = DATA.categories && DATA.categories.length
      ? DATA.categories : Array.from(new Set(RAW.map(function (q) { return q.category; })));
    $('cat-bars').innerHTML = cats.map(function (c) {
      var items = RAW.filter(function (q) { return q.category === c; });
      var m = items.filter(function (q) { return recOf(q.id).box >= 4; }).length;
      return bar(c, m + '/' + items.length, Math.round(m / items.length * 100));
    }).join('');

    $('box-bars').innerHTML = [0, 1, 2, 3, 4, 5].map(function (b) {
      var n = RAW.filter(function (q) { return recOf(q.id).box === b; }).length;
      return bar('Box ' + b + (b === 5 ? '（已记住）' : ''), n + ' 题', Math.round(n / RAW.length * 100));
    }).join('');
  }
  function bar(name, num, pct) {
    return '<div class="bar-row"><span class="name">' + esc(name) + '</span>' +
      '<span class="bar-track"><span class="bar-fill" style="width:' + pct + '%"></span></span>' +
      '<span class="num">' + num + '</span></div>';
  }

  // ---------------- 编辑 ----------------
  function openEditor() {
    if (!state.current) return;
    var c = cardOf(state.current);
    $('edit-q').value = c.question;
    $('edit-a').value = c.answer;
    $('modal').classList.remove('hidden');
  }
  function closeEditor() { $('modal').classList.add('hidden'); }

  // ---------------- Toast ----------------
  var toastTimer;
  function toast(msg) {
    var t = $('toast');
    t.textContent = msg;
    t.classList.remove('hidden');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.add('hidden'); }, 1800);
  }

  // ---------------- 事件 ----------------
  function bind() {
    $('tabs').addEventListener('click', function (e) {
      var btn = e.target.closest('.tab');
      if (!btn) return;
      var mode = btn.dataset.mode;
      state.mode = mode;
      Array.prototype.forEach.call(document.querySelectorAll('.tab'), function (b) {
        b.classList.toggle('active', b.dataset.mode === mode);
      });
      Array.prototype.forEach.call(document.querySelectorAll('.view'), function (v) {
        v.classList.toggle('active', v.id === 'view-' + mode);
      });
      if (mode === 'stats') renderStats();
      if (mode === 'browse') renderList();
    });

    $('cat-filter').addEventListener('change', function () {
      state.category = this.value; state.dueOnly = $('due-only').checked;
      refreshMeta(); buildQueue();
    });
    $('due-only').addEventListener('change', function () {
      state.dueOnly = this.checked; buildQueue();
    });
    $('cat-filter2').addEventListener('change', renderList);
    $('search').addEventListener('input', renderList);

    $('btn-ai').addEventListener('click', judge);
    $('btn-show').addEventListener('click', reveal);
    $('btn-again').addEventListener('click', function () { grade(0); });
    $('btn-hard').addEventListener('click', function () { grade(1); });
    $('btn-good').addEventListener('click', function () { grade(2); });
    $('btn-skip').addEventListener('click', function () { state.cursor++; nextCard(); });
    $('btn-edit').addEventListener('click', openEditor);
    $('btn-reset').addEventListener('click', function () {
      if (!state.current) return;
      delete progress[state.current.id];
      save(STORE_KEY, progress);
      toast('已重置这张卡的进度');
      refreshMeta(); nextCard();
    });

    $('answer-input').addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); judge(); }
    });

    $('btn-chat-send').addEventListener('click', sendChat);
    $('btn-dig').addEventListener('click', function () {
      followUp('（候选人暂时没答上来，请给一点提示引导，然后换个角度继续深挖。）');
    });
    $('chat-input').addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); sendChat(); }
    });

    $('list').addEventListener('click', function (e) {
      var item = e.target.closest('.item');
      if (!item) return;
      item.querySelector('.a').classList.toggle('collapsed');
    });

    $('edit-cancel').addEventListener('click', closeEditor);
    $('edit-save').addEventListener('click', function () {
      if (!state.current) return;
      overrides[state.current.id] = {
        question: $('edit-q').value.trim(), answer: $('edit-a').value.trim()
      };
      save(OVERRIDE_KEY, overrides);
      closeEditor(); nextCard(); toast('已保存（仅本地生效）');
    });
    $('edit-revert').addEventListener('click', function () {
      if (!state.current) return;
      delete overrides[state.current.id];
      save(OVERRIDE_KEY, overrides);
      closeEditor(); nextCard(); toast('已还原');
    });

    $('ai-btn').addEventListener('click', openAiModal);
    $('ai-cancel').addEventListener('click', closeAiModal);
    $('ai-save').addEventListener('click', function () {
      aiConf = {
        base: $('ai-base').value.trim().replace(/\/+$/, ''),
        key: $('ai-key').value.trim(),
        model: $('ai-model').value.trim()
      };
      save(AI_KEY, aiConf);
      closeAiModal();
      toast(aiConf.base && aiConf.key ? 'AI 判卷已就绪' : '配置不完整');
    });

    $('btn-export').addEventListener('click', function () {
      var blob = new Blob([JSON.stringify({ progress: progress, overrides: overrides }, null, 2)],
        { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'quiz-progress-' + new Date().toISOString().slice(0, 10) + '.json';
      a.click();
    });
    $('btn-import').addEventListener('click', function () { $('file-import').click(); });
    $('file-import').addEventListener('change', function () {
      var f = this.files[0];
      if (!f) return;
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var data = JSON.parse(reader.result);
          if (data.progress) { progress = data.progress; save(STORE_KEY, progress); }
          if (data.overrides) { overrides = data.overrides; save(OVERRIDE_KEY, overrides); }
          toast('导入成功'); renderStats(); refreshMeta();
        } catch (e) { toast('文件格式不对'); }
      };
      reader.readAsText(f);
    });

    $('theme-btn').addEventListener('click', function () {
      var dark = document.body.classList.toggle('dark');
      localStorage.setItem(THEME_KEY, dark ? 'dark' : 'light');
    });

    document.addEventListener('keydown', function (e) {
      var modalOpen = !$('modal').classList.contains('hidden') || !$('ai-modal').classList.contains('hidden');
      if (modalOpen) {
        if (e.key === 'Escape') { closeEditor(); closeAiModal(); }
        return;
      }
      if (state.mode !== 'review') return;
      var typing = e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA';
      if (e.key === '1') { grade(0); return; }
      if (e.key === '2') { grade(1); return; }
      if (e.key === '3') { grade(2); return; }
      if (typing) return;
      if (e.code === 'Space') {
        e.preventDefault();
        if (!state.revealed) reveal(); else { state.cursor++; nextCard(); }
      } else if (e.key.toLowerCase() === 'e') { openEditor(); }
    });

    Array.prototype.forEach.call(document.querySelectorAll('.btn'), function (b) {
      b.addEventListener('focus', function () { b.blur(); });
    });
  }

  // ---------------- 启动 ----------------
  function init() {
    if (localStorage.getItem(THEME_KEY) === 'dark') document.body.classList.add('dark');
    initFilters();
    refreshMeta();
    bind();
    buildQueue();
  }
  init();
})();
