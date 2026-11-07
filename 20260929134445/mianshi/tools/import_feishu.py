# -*- coding: utf-8 -*-
"""
把飞书知识库导出包转换成 Markdown，并抽成面试问答卡。

用法:
    python tools/import_feishu.py                # 转换并生成题库
    python tools/import_feishu.py --dry-run      # 只看结果不写文件
    python tools/import_feishu.py --export-dir D:\\tmp\\feishu
"""
from __future__ import annotations

import argparse
import html as html_lib
import json
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORT_DIR = ROOT / "feishu_export"
RAW_DIR = ROOT / ".cache" / "unzipped"
CONTENT_DIR = ROOT / "content"
DATA_FILE = ROOT / "data" / "quiz-data.js"

TEXT_EXTS = {".md", ".markdown", ".txt"}
HTML_EXTS = {".html", ".htm", ".xhtml"}
DOCX_EXTS = {".docx"}
PDF_EXTS = {".pdf"}
SKIP_NAMES = {"index", "toc", "readme", "目录"}

Q_PATTERN = re.compile(r"^\s*(?:#{1,6}\s*)?[（(]?(?:Q|q|问|问题|题目|面试题)[）)]?\s*[:：]\s*(.+?)\s*$")
A_PATTERN = re.compile(r"^\s*(?:#{1,6}\s*)?[（(]?(?:A|a|答|答案|解答|解析)[）)]?\s*[:：]\s*(.*)$")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
QA_MARK_HINT = re.compile(r"(问\s*[:：]|答\s*[:：]|Q\s*[:：]|A\s*[:：])")

# 不进题库：项目复盘（旧项目）、简历/AI 探索等杂项（白名单优先）
EXCLUDE_PATTERN = re.compile(
    r"项目|实战|画像|信贷|电商|简历|AI提效|AI在大数据|SKILL|公司架构|职业划分|"
    r"流程图|画板|准备的东西|探索", re.I)
EXCLUDE_WHITELIST = ("面试题技巧", "涤生大数据", "简历与面试")

# 分类规则：按主题归大类（顺序敏感，命中即停）
CAT_RULES = [
    (re.compile(r"hive", re.I), "Hive"),
    (re.compile(r"flink", re.I), "Flink"),
    (re.compile(r"spark", re.I), "Spark"),
    (re.compile(r"doris", re.I), "Doris"),
    (re.compile(r"scala|scale", re.I), "Scala"),
    (re.compile(r"linux", re.I), "Linux"),
    (re.compile(r"kafka", re.I), "Kafka"),
    (re.compile(r"hadoop|hdfs|zookeeper", re.I), "Hadoop/ZK"),
    (re.compile(r"java", re.I), "Java"),
    (re.compile(r"mysql", re.I), "MySQL"),
    (re.compile(r"sql", re.I), "SQL"),
    (re.compile(r"python", re.I), "Python"),
    (re.compile(r"数仓|数据仓库|数据治理|数据采集|OneData|维度建模|数据倾斜|商业化|主题域", re.I), "数仓"),
    (re.compile(r"面试|错题|查漏|面经|参考", re.I), "面试综合"),
]

# 题型标签：面试题（现成问答）vs 理论（笔记要点）
TYPE_RULE = re.compile(r"面试|八股|错题|查漏|面经|题|记录", re.I)

# 标题腔前缀噪音：「面试补充：行列过滤」→「行列过滤」
PREFIX_NOISE = re.compile(
    r"^(?:面试补充|面试相关|面试问题|面试题|面试|补充|扩展|延伸|复习|知识点|"
    r"基础|进阶|重点|难点|总结)[:：]\s*·?\s*")


# --------------------------------------------------------------------------
# 解压
# --------------------------------------------------------------------------
def unzip_all(export_dir: Path, raw_dir: Path) -> int:
    count = 0
    for zf in sorted(export_dir.rglob("*.zip")):
        target = raw_dir / zf.stem
        target.mkdir(parents=True, exist_ok=True)
        try:
            with zipfile.ZipFile(zf) as z:
                for name in z.namelist():
                    if name.endswith("/"):
                        continue
                    out = target / safe_name(name)
                    out.parent.mkdir(parents=True, exist_ok=True)
                    with z.open(name) as src, open(out, "wb") as dst:
                        dst.write(src.read())
                count += 1
                print(f"  [解压] {zf.name} -> {target.relative_to(ROOT)}")
        except zipfile.BadZipFile:
            print(f"  [跳过] {zf.name} 不是有效 zip")
    return count


def safe_name(name: str) -> str:
    name = name.replace("\\", "/").lstrip("/")
    name = re.sub(r"[<>:\"|?*]", "_", name)
    return name


# --------------------------------------------------------------------------
# 格式转换
# --------------------------------------------------------------------------
def html_to_markdown(raw: str) -> str:
    body = extract_body(raw)
    try:
        import html2text

        h = html2text.HTML2Text()
        h.body_width = 0
        h.ignore_images = True
        h.ignore_emphasis = False
        h.single_line_break = False
        return h.handle(body)
    except Exception:
        pass
    try:
        from markdownify import markdownify

        return markdownify(body, heading_style="ATX")
    except Exception:
        pass
    return html_fallback(body)


def extract_body(raw: str) -> str:
    m = re.search(r"<body[^>]*>([\s\S]*?)</body>", raw, re.I)
    body = m.group(1) if m else raw
    body = re.sub(r"<(script|style|noscript)[^>]*>[\s\S]*?</\1>", "", body, flags=re.I)
    return body


def html_fallback(body: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", body, flags=re.I)
    text = re.sub(r"</?(p|div|section|tr)[^>]*>", "\n\n", text, flags=re.I)
    text = re.sub(r"<h([1-6])[^>]*>([\s\S]*?)</h\1>",
                  lambda m: "\n\n" + "#" * int(m.group(1)) + " " + m.group(2).strip() + "\n\n",
                  text, flags=re.I)
    text = re.sub(r"<li[^>]*>([\s\S]*?)</li>", lambda m: "\n- " + m.group(1).strip(), text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    return html_lib.unescape(text)


def docx_to_markdown(path: Path) -> str:
    try:
        import mammoth

        with open(path, "rb") as f:
            result = mammoth.convert_to_html(f)
        return html_to_markdown(result.value)
    except Exception:
        pass
    try:
        import docx  # python-docx

        doc = docx.Document(str(path))
        lines = []
        for p in doc.paragraphs:
            text = p.text.strip()
            if not text:
                continue
            style = (p.style.name or "").lower()
            m = re.search(r"heading\s*(\d)", style)
            if m:
                level = min(int(m.group(1)), 6)
                lines.append("#" * level + " " + text)
            elif style.startswith("list"):
                lines.append("- " + text)
            else:
                lines.append(text)
            lines.append("")
        return "\n".join(lines)
    except Exception:
        return ""


# PDF 页眉页脚/导航噪音
PDF_NOISE = re.compile(
    r"^(?:页面[/\\]|主页[/\\]|由 .*(?:创建|修改)|最后修改于|Update$|Review$|"
    r"尖叫提醒$|健哥$|光哥$|update\s*\d{4}.*$|\d{1,3}$)", re.I)


def pdf_to_markdown(path: Path) -> str:
    """飞书导出的题库 PDF：编号题目行 -> ### 标题，其余做正文。"""
    import pymupdf

    doc = pymupdf.open(str(path))
    out = []
    for page in doc:
        for raw in page.get_text("text").split("\n"):
            ln = raw.strip()
            if not ln or PDF_NOISE.match(ln):
                continue
            m = re.match(r"^(\d+(?:\.\d+)*)\s*[、.．,，]?\s*(.+)$", ln)
            if m:
                title = m.group(2).strip()
                # 正文列表（如「1. 尖叫提示: ...」）不当题目
                if len(title) >= 6 and "尖叫提示" not in title:
                    out.append("")
                    out.append("### " + title)
                    continue
            out.append(ln)
        out.append("")
    doc.close()
    return "\n".join(out)


def clean_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.strip()


# --------------------------------------------------------------------------
# 问答抽取
# --------------------------------------------------------------------------
def split_sections(md: str):
    """按标题切成 (层级, 标题, 正文) 列表，正文含其下所有子内容。"""
    lines = md.split("\n")
    sections = []
    cur_level, cur_title, cur_body = 0, "", []
    for line in lines:
        m = HEADING_PATTERN.match(line)
        if m:
            sections.append((cur_level, cur_title, "\n".join(cur_body)))
            cur_level, cur_title, cur_body = len(m.group(1)), m.group(2).strip(), []
        else:
            cur_body.append(line)
    sections.append((cur_level, cur_title, "\n".join(cur_body)))
    return [(lv, t, b.strip()) for lv, t, b in sections if t or b.strip()]


def parse_explicit_qa(md: str):
    """规则一：显式 Q:/A: 配对。"""
    cards = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        mq = Q_PATTERN.match(lines[i])
        if not mq:
            i += 1
            continue
        question = mq.group(1).strip()
        answer_lines = []
        i += 1
        while i < len(lines):
            line = lines[i]
            if Q_PATTERN.match(line):
                break
            ma = A_PATTERN.match(line)
            if ma:
                answer_lines.append(ma.group(1))
            elif HEADING_PATTERN.match(line):
                break
            else:
                answer_lines.append(line)
            i += 1
        answer = "\n".join(answer_lines).strip()
        if question and answer:
            cards.append((question, answer))
    return cards


def parse_heading_qa(md: str):
    """规则二：### 及以下标题当问题，其下正文当答案。"""
    cards = []
    for level, title, body in split_sections(md):
        if level < 2 or not title:
            continue
        body = body.strip()
        if len(re.sub(r"\s", "", body)) < 20:
            continue
        if title.lower() in SKIP_NAMES:
            continue
        cards.append((title, body))
    return cards


def parse_outline_cards(md: str, source_title: str):
    """规则三：兜底，二级及以下小标题 -> 要点卡。"""
    cards = []
    for level, title, body in split_sections(md):
        if level < 2 or not title:
            continue
        bullets = [ln.strip()[2:].strip() for ln in body.split("\n") if re.match(r"^\s*[-*+]\s+\S", ln)]
        summary = "\n".join("- " + b for b in bullets[:8]) if bullets else body[:600]
        if not summary.strip():
            continue
        cards.append((title, summary))
    return cards


def extract_cards(md: str, source: str, category: str):
    """按优先级选一种抽取方式。"""
    title = first_heading(md) or Path(source).stem

    if QA_MARK_HINT.search(md):
        pairs = parse_explicit_qa(md)
        if pairs:
            return pairs, "explicit"

    pairs = parse_heading_qa(md)
    if pairs:
        # 文档本身是「一标题一答案」的结构
        return [(f"{title} · {q}" if title and q != title else q, a) for q, a in pairs], "heading"

    pairs = parse_outline_cards(md, title)
    return pairs, "outline"


def first_heading(md: str) -> str:
    for line in md.split("\n"):
        m = HEADING_PATTERN.match(line)
        if m:
            return m.group(2).strip()
    return ""


def guess_category(rel_path: Path) -> str:
    """目录名优先，其次文件名；都没命中归「其他」。"""
    for part in rel_path.parts[:-1]:
        for pat, cat in CAT_RULES:
            if pat.search(part):
                return cat
    stem = rel_path.stem
    for pat, cat in CAT_RULES:
        if pat.search(stem):
            return cat
    return "其他"


def guess_type(rel_path: Path) -> str:
    return "面试题" if TYPE_RULE.search(rel_path.stem) else "理论"


def is_excluded(rel_path: Path) -> bool:
    name = rel_path.name
    if any(w in name for w in EXCLUDE_WHITELIST):
        return False
    return bool(EXCLUDE_PATTERN.search(name))


# --------------------------------------------------------------------------
# 主流程
# --------------------------------------------------------------------------
def collect_files(export_dir: Path, raw_dir: Path):
    files = []
    for base in (export_dir, raw_dir):
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file():
                continue
            ext = p.suffix.lower()
            if ext in TEXT_EXTS | HTML_EXTS | DOCX_EXTS | PDF_EXTS and p.name.lower() != "quiz-data.js":
                files.append((p, base))
    # 去重：解压目录优先
    seen, uniq = set(), []
    for p, base in files:
        key = p.name
        if key in seen:
            continue
        seen.add(key)
        uniq.append((p, base))
    return uniq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--export-dir", default=str(EXPORT_DIR))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    export_dir = Path(args.export_dir)
    if not export_dir.exists():
        print(f"[提示] 还没找到 {export_dir}，请先按 README 把飞书导出的 zip 放进去。")
        export_dir.mkdir(parents=True, exist_ok=True)

    print("1) 解压导出包")
    n_zip = unzip_all(export_dir, RAW_DIR)

    print("2) 扫描文件")
    files = collect_files(export_dir, RAW_DIR)
    if not files:
        print(f"[空] {export_dir} 里没有可转换的文件。把 zip 或 md/html/docx 放进来再跑一次。")
        return 0
    print(f"   共 {len(files)} 个文件（zip {n_zip} 个）")

    print("3) 转换并抽题")
    if not args.dry_run:
        CONTENT_DIR.mkdir(parents=True, exist_ok=True)
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    questions = []
    seen_questions = set()
    stat = {"explicit": 0, "heading": 0, "outline": 0, "skipped": 0, "excluded": 0}
    qid = 0

    for path, base in files:
        if is_excluded(path.relative_to(base)):
            stat["excluded"] += 1
            continue
        ext = path.suffix.lower()
        try:
            if ext in TEXT_EXTS:
                md = path.read_text(encoding="utf-8", errors="ignore")
            elif ext in HTML_EXTS:
                md = html_to_markdown(path.read_text(encoding="utf-8", errors="ignore"))
            elif ext in PDF_EXTS:
                md = pdf_to_markdown(path)
            else:
                md = docx_to_markdown(path)
        except Exception as e:  # noqa: BLE001
            print(f"   [失败] {path.name}: {e}")
            stat["skipped"] += 1
            continue

        md = clean_markdown(md)
        if len(md) < 30:
            stat["skipped"] += 1
            continue

        rel = path.relative_to(base)
        category = guess_category(rel)
        pairs, kind = extract_cards(md, str(rel), category)
        stat[kind] += 1 if pairs else 0
        if not pairs:
            stat["skipped"] += 1
            continue

        if not args.dry_run:
            out = CONTENT_DIR / rel.with_suffix(".md")
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8")

        for q, a in pairs:
            q = q.replace("**", "").replace("`", "").strip().strip("· ").strip()
            q = PREFIX_NOISE.sub("", q).strip().strip("· ").strip()
            # 清理噪音：空标题（如「问题发现：」）、超短问题、重复问题
            if not q or len(q) < 5 or q.endswith(("：", ":")):
                continue
            if q in seen_questions:
                continue
            seen_questions.add(q)
            qid += 1
            questions.append({
                "id": f"q{qid:04d}",
                "category": category,
                "type": guess_type(rel),
                "question": q,
                "answer": a.strip(),
                "source": str(rel),
            })

    print(f"   抽到 {len(questions)} 张卡 "
          f"(显式问答 {stat['explicit']} 篇 / 标题式 {stat['heading']} 篇 / 要点式 {stat['outline']} 篇 / "
          f"跳过 {stat['skipped']} 篇 / 排除 {stat['excluded']} 篇)")

    if args.dry_run:
        for item in questions[:5]:
            print(f"   - [{item['category']}] {item['question'][:50]} -> {item['answer'][:40]}...")
        print("[dry-run] 未写入任何文件")
        return 0

    categories = sorted({q["category"] for q in questions})
    types = sorted({q.get("type", "理论") for q in questions})
    payload = {
        "generatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "categories": categories,
        "types": types,
        "questions": questions,
    }
    DATA_FILE.write_text(
        "window.QUIZ_DATA = " + json.dumps(payload, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )
    print(f"4) 已写入 {DATA_FILE.relative_to(ROOT)}")
    print("   现在双击打开 src/index.html 就可以开始自测了。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
