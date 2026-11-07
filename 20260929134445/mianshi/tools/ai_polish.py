# -*- coding: utf-8 -*-
"""
AI 把题库转化成「面试问答」形态。

两种模式：
  --mode qa     （推荐）把「理论卡」整体转化：笔记标题 → 面试官自然问法，
                笔记内容 → 分点标准答案（不编造、不丢要点），type 改为面试题
  --mode polish 只把标题腔问题改写成自然问法，不动答案

已经是自然问句的题目在 polish 模式下自动跳过；qa 模式处理全部理论卡。
支持断点续跑：中断后重跑自动继续。

配置（三选一）：
  命令行: --base https://open.bigmodel.cn/api/paas/v4 --key xxx --model glm-4-flash
  环境变量: AI_BASE / AI_KEY / AI_MODEL

用法：
  python tools/ai_polish.py --mode qa --dry-run   # 预览范围
  python tools/ai_polish.py --mode qa             # 开始转化
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "quiz-data.js"
BATCH = {"qa": 8, "polish": 15}

NATURAL = re.compile(
    r"[?？]|吗[。？?]?|什么|怎么|怎样|如何|为什么|哪些|哪种|说说|讲讲|聊聊|"
    r"介绍(一下)?|谈谈|描述(一下)?|对比|区别|原因|场景|方案|流程|过程|原理|"
    r"实现(一下|过)?|解决|处理|优化|排查|设计", re.I)

PROMPT_POLISH = (
    "你是面试题库编辑。把下面从笔记标题提炼的「题目」改写成面试官的口语化提问，"
    "要求：考察点完全不变，不新增知识点；像真人面试官随口问出来的；一句话，20 字左右。"
    "输出 JSON 数组 [{\"id\": 原id, \"q\": \"改写后的问题\"}]，不要输出任何其他文字。"
)

PROMPT_QA = (
    "你是大数据方向的高级面试官和题库编辑。输入是候选人自己整理的知识点卡片"
    "（标题比较干巴，内容是原始笔记）。请把每张卡转化为一道「面试问答」：\n"
    "1. q：把标题改写成面试官的真实问法（口语、自然、考察点不变，25 字左右，"
    "可以是追问式，比如「生产上遇到数据倾斜你是怎么定位和解决的？」）；\n"
    "2. a：基于原始笔记整理出一份适合口头作答的面试标准答案：分点、简洁、"
    "保留笔记里的全部关键要点和数字细节，绝不编造笔记里没有的内容；"
    "如果笔记内容太少，就基于该知识点补充最基本的完整回答，但要在末尾加一句"
    "「（原笔记较简略，此答案有 AI 补充）」。\n"
    "输出 JSON 数组 [{\"id\": 原id, \"q\": \"...\", \"a\": \"...\"}]，不要输出任何其他文字。"
)


def load_data():
    s = DATA_FILE.read_text(encoding="utf-8")
    return json.loads(s[s.index("=") + 1:].rstrip(";\n"))


def save_data(payload):
    DATA_FILE.write_text(
        "window.QUIZ_DATA = " + json.dumps(payload, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )


def call_ai(base, key, model, messages, timeout=120):
    url = base.rstrip("/") + "/chat/completions"
    body = json.dumps({"model": model, "temperature": 0.3, "messages": messages}).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", "Bearer " + key)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def extract_json(text):
    m = re.search(r"\[[\s\S]*\]", text)
    if not m:
        return None
    try:
        return json.loads(m[0])
    except Exception:
        return None


def load_ai_config():
    """默认从 tools/ai-config.json 读，命令行参数 > 环境变量 > 配置文件。"""
    cfg_file = Path(__file__).resolve().parent / "ai-config.json"
    if cfg_file.exists():
        try:
            return json.loads(cfg_file.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def main():
    cfg = load_ai_config()
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["qa", "polish"], default="qa")
    ap.add_argument("--base", default=os.environ.get("AI_BASE") or cfg.get("base", ""))
    ap.add_argument("--key", default=os.environ.get("AI_KEY") or cfg.get("key", ""))
    ap.add_argument("--model", default=os.environ.get("AI_MODEL") or cfg.get("model", ""))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--category", help="只处理指定分类（如 Hive），可逗号分隔多个")
    args = ap.parse_args()

    payload = load_data()
    questions = payload["questions"]
    progress_file = ROOT / "data" / (".genqa-progress.json" if args.mode == "qa"
                                     else ".polish-progress.json")
    progress = json.loads(progress_file.read_text(encoding="utf-8")) if progress_file.exists() else {}

    if args.mode == "qa":
        todo = [q for q in questions
                if (q.get("type") == "理论" or " · " in q["question"])
                and q["id"] not in progress]
        if args.category:
            cats = {c.strip() for c in args.category.split(",")}
            todo = [q for q in todo if q["category"] in cats]
    else:
        todo = [q for q in questions
                if not NATURAL.search(q["question"]) and q["id"] not in progress]

    batch = BATCH[args.mode]
    print(f"模式 {args.mode}：题库 {len(questions)} 题，待处理 {len(todo)} 题"
          f"（已完成 {len(progress)}，批大小 {batch}）")
    if args.dry_run:
        for q in todo[:15]:
            print(f"  [{q['category']}] {q['question']}")
        if len(todo) > 15:
            print("  ...")
        return 0

    if not (args.base and args.key and args.model):
        ap.error("缺少 AI 配置：--base/--key/--model 或环境变量 AI_BASE/AI_KEY/AI_MODEL")

    prompt = PROMPT_QA if args.mode == "qa" else PROMPT_POLISH
    done = 0
    for i in range(0, len(todo), batch):
        items = [{"id": q["id"], "q": q["question"], **({"a": q["answer"]} if args.mode == "qa" else {})}
                 for q in todo[i:i + batch]]
        try:
            text = call_ai(args.base, args.key, args.model,
                           [{"role": "system", "content": prompt},
                            {"role": "user", "content": json.dumps(items, ensure_ascii=False)}])
        except Exception as e:  # noqa: BLE001
            print(f"  [批次 {i // batch + 1} 失败] {e}，10 秒后继续（Ctrl+C 可中断，进度已保存）")
            time.sleep(10)
            continue

        result = extract_json(text) or []
        n = 0
        for item in result:
            qid = str(item.get("id", ""))
            nq = str(item.get("q", "")).strip()
            if not qid or len(nq) < 5:
                continue
            progress[qid] = {"q": nq}
            if args.mode == "qa" and len(str(item.get("a", "")).strip()) >= 20:
                progress[qid]["a"] = str(item["a"]).strip()
            n += 1
        done += n
        print(f"  进度 {min(i + batch, len(todo))}/{len(todo)}  本批完成 {n} 题")
        progress_file.write_text(json.dumps(progress, ensure_ascii=False, indent=1),
                                 encoding="utf-8")
        time.sleep(0.5)

    changed = 0
    for q in questions:
        p = progress.get(q["id"])
        if not p:
            continue
        q["question"] = p["q"]
        if p.get("a"):
            q["answer"] = p["a"]
        if args.mode == "qa":
            q["type"] = "面试题"
            q["aiPolished"] = True
        changed += 1

    payload["types"] = sorted({q.get("type", "理论") for q in questions})
    save_data(payload)
    print(f"\n完成：本轮 {done} 题，累计 {changed} 题，已写回 {DATA_FILE.name}")
    print("刷新页面即可。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
