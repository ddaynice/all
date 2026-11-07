# -*- coding: utf-8 -*-
"""题库检索索引（RAG 的"R"）。

把 content/ 下的 Markdown 按"标题段落"切块，建入 SQLite FTS5（trigram 分词，
对中文子串匹配友好）。检索入口是 search()；将来若升级向量检索（ChromaDB +
bge-small-zh），只需替换这个函数的内部实现，server.py 不用动。

命令行手动重建索引：
    python -m app.indexer           # 有索引则跳过
    python -m app.indexer --force   # 强制重建
"""
import argparse
import re
import sqlite3
from contextlib import closing
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent        # mianshi/
CONTENT_DIR = BASE_DIR / "content"
KB_PATH = Path(__file__).resolve().parent / "data" / "kb.db"

CHUNK_MIN_LEN = 40      # 太短的段落不入库
CHUNK_MAX_LEN = 1600    # 单块截断，避免撑爆提示词


def chunks_from_file(path: Path) -> list[dict]:
    """按标题层级切块：每块 = 最后两级标题路径 + 该节正文。"""
    rel = path.relative_to(CONTENT_DIR).as_posix()
    text = path.read_text(encoding="utf-8", errors="ignore")
    out: list[dict] = []
    stack: list[tuple[int, str]] = []   # (标题级别, 标题文字)
    buf: list[str] = []

    def flush():
        body = "\n".join(buf).strip()
        buf.clear()
        if len(body) < CHUNK_MIN_LEN:
            return
        title = " / ".join(h for _, h in stack[-2:]) if stack else rel
        out.append({"source": rel, "title": title or rel, "content": body[:CHUNK_MAX_LEN]})

    for line in text.splitlines():
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush()
            level = len(m.group(1))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, m.group(2).strip()))
        else:
            buf.append(line)
    flush()
    return out


def build(force: bool = False) -> int:
    """构建/更新索引，返回片段总数。已有索引且未 force 时直接跳过。"""
    KB_PATH.parent.mkdir(exist_ok=True)
    with closing(sqlite3.connect(KB_PATH)) as conn, conn:
        conn.execute(
            "CREATE VIRTUAL TABLE IF NOT EXISTS kb USING fts5("
            "source, title, content, tokenize='trigram')"
        )
        count = conn.execute("SELECT COUNT(*) FROM kb").fetchone()[0]
        if count and not force:
            return count
        conn.execute("DELETE FROM kb")
        rows = []
        for md in sorted(CONTENT_DIR.rglob("*.md")):
            for c in chunks_from_file(md):
                rows.append((c["source"], c["title"], c["content"]))
        conn.executemany("INSERT INTO kb(source, title, content) VALUES(?, ?, ?)", rows)
        return len(rows)


def search(query: str, k: int = 4) -> list[dict]:
    """检索最相关的 k 个片段。查询为空或索引为空时返回 []。"""
    terms = re.findall(r"[\w\u4e00-\u9fff]{2,}", query)
    if not terms:
        return []
    seen, uniq = set(), []
    for t in terms:
        low = t.lower()
        if low not in seen:
            seen.add(low)
            uniq.append(t)
    match = " OR ".join('"%s"' % t.replace('"', '""') for t in uniq[:8])
    try:
        with closing(sqlite3.connect(KB_PATH)) as conn:
            rows = conn.execute(
                "SELECT source, title, content FROM kb WHERE kb MATCH ? "
                "ORDER BY rank LIMIT ?",
                (match, k),
            ).fetchall()
    except sqlite3.OperationalError:
        return []
    return [{"source": r[0], "title": r[1], "content": r[2]} for r in rows]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="强制重建索引")
    args = parser.parse_args()
    n = build(force=args.force)
    print(f"索引就绪：{n} 个片段 → {KB_PATH}")
