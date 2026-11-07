# -*- coding: utf-8 -*-
"""个人 AI 平台服务入口。

职责：
- 统一入口 + 邀请码登录（Cookie 会话）
- 工具静态托管（门户 / 刷题 / AI 陪练）
- AI 网关：所有工具的 AI 请求统一走 /api/chat（将来加限流/计费只改这里）
- SQLite 存储：对话历史（所有表预留 user_id 列，为多用户升级做准备）
"""
import hmac
import json
import os
import re
import secrets
import sqlite3
import subprocess
import sys
import threading
import time
from contextlib import closing
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import (
    FileResponse,
    JSONResponse,
    RedirectResponse,
    StreamingResponse,
)
from fastapi.staticfiles import StaticFiles

from app import indexer
from app.config import TOOLS

# ---------- 路径与配置 ----------
BASE_DIR = Path(__file__).resolve().parent.parent        # mianshi/
PLATFORM_DIR = Path(__file__).resolve().parent           # platform/
DATA_DIR = PLATFORM_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
load_dotenv(PLATFORM_DIR / ".env")

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "").strip()
DEEPSEEK_BASE = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
INVITE_CODE = os.getenv("INVITE_CODE", "").strip()
PORT = int(os.getenv("PORT", "8600"))

# 飞书凭证（选填）：配置后「资料同步」会先自动拉取最新文档
FEISHU_APP_ID = os.getenv("FEISHU_APP_ID", "").strip()
FEISHU_APP_SECRET = os.getenv("FEISHU_APP_SECRET", "").strip()
FEISHU_SPACE_ID = os.getenv("FEISHU_SPACE_ID", "").strip()

COOKIE_NAME = "p_session"
USER_ID = "me"  # 将来接入真实账号体系后，替换为当前登录用户 id

# ---------- 会话密钥（首次启动自动生成） ----------
_secret_file = DATA_DIR / "secret.key"
if _secret_file.exists():
    _SECRET = _secret_file.read_text().strip()
else:
    _SECRET = secrets.token_hex(32)
    _secret_file.write_text(_SECRET)

SESSION_TOKEN = hmac.new(_SECRET.encode(), b"platform-session-v1", "sha256").hexdigest()

# ---------- 数据库 ----------
DB_PATH = DATA_DIR / "platform.db"


def db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db() -> None:
    with closing(db()) as conn, conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS conversations(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL DEFAULT 'me',
                title TEXT NOT NULL DEFAULT '新对话',
                created_at REAL NOT NULL
            );
            CREATE TABLE IF NOT EXISTS messages(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL DEFAULT 'me',
                conversation_id INTEGER NOT NULL
                    REFERENCES conversations(id) ON DELETE CASCADE,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at REAL NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_msg_conv ON messages(conversation_id);
            """
        )
        try:  # 旧库升级：追加参考来源列
            conn.execute("ALTER TABLE messages ADD COLUMN sources TEXT NOT NULL DEFAULT ''")
        except sqlite3.OperationalError:
            pass


init_db()

# ---------- 知识库检索索引（RAG）：首次启动自动构建 ----------
# 以后新增了题库文档，运行 python -m app.indexer --force 重建
_KB_ROWS = indexer.build()
print(f"[kb] 题库索引就绪：{_KB_ROWS} 个片段")

# ---------- AI 人设预设：新工具接入 AI 只需在这里加一段提示词 ----------
MODES = {
    "interviewer": (
        "你是一位资深的大数据方向技术面试官，精通 Hadoop/Hive/Spark/Flink/Kafka/"
        "Doris/StarRocks、数仓建模、SQL 与 Java 基础。请扮演面试官对用户进行模拟面试："
        "一次只问一个问题；用户作答后，先简短点评（答对了什么、漏了什么），"
        "给出参考答案要点，再自然引出下一个相关或更深入的问题。"
        "语气专业友善，像真实面试一样循序渐进，从基础逐步加深。"
    ),
    "explain": (
        "你是资深大数据工程师与技术导师，精通 Hadoop/Hive/Spark/Flink/Kafka/Doris、"
        "数仓建模与 SQL。用户会提出技术问题或请求讲解面试题，"
        "请给出结构化、由浅入深的讲解，适当举例、给记忆要点和易错点。用中文回答。"
    ),
    "free": "你是一个乐于助人的中文 AI 助手，回答力求准确、简洁、结构清晰。",
}
DEFAULT_MODE = "interviewer"

# ---------- 应用与鉴权 ----------
app = FastAPI(title="我的 AI 平台")

PUBLIC_PATHS = {"/login", "/api/login", "/favicon.ico"}


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    path = request.url.path
    if path in PUBLIC_PATHS:
        return await call_next(request)
    if request.cookies.get(COOKIE_NAME) == SESSION_TOKEN:
        return await call_next(request)
    if path.startswith("/api"):
        return JSONResponse({"detail": "未登录"}, status_code=401)
    return RedirectResponse("/login")


# ---------- 登录 ----------
@app.get("/login")
async def login_page():
    return FileResponse(PLATFORM_DIR / "static" / "login.html")


@app.post("/api/login")
async def api_login(request: Request):
    body = await request.json()
    code = (body or {}).get("code", "")
    if not INVITE_CODE:
        return JSONResponse(
            {"detail": "服务端未配置 INVITE_CODE，请编辑 app/.env"}, status_code=500
        )
    if hmac.compare_digest(code, INVITE_CODE):
        resp = JSONResponse({"ok": True})
        resp.set_cookie(
            COOKIE_NAME, SESSION_TOKEN,
            max_age=30 * 24 * 3600, httponly=True, samesite="lax",
        )
        return resp
    return JSONResponse({"detail": "邀请码不正确"}, status_code=403)


@app.post("/api/logout")
async def api_logout():
    resp = JSONResponse({"ok": True})
    resp.delete_cookie(COOKIE_NAME)
    return resp


# ---------- 门户 ----------
@app.get("/")
async def portal():
    return FileResponse(PLATFORM_DIR / "static" / "index.html")


@app.get("/api/tools")
async def api_tools():
    return TOOLS


@app.get("/api/me")
async def api_me():
    return {"user_id": USER_ID, "ai_configured": bool(DEEPSEEK_API_KEY)}


# ---------- 对话历史 ----------
@app.get("/api/conversations")
async def list_conversations():
    with closing(db()) as conn:
        rows = conn.execute(
            "SELECT c.id, c.title, c.created_at, COUNT(m.id) AS msg_count "
            "FROM conversations c LEFT JOIN messages m ON m.conversation_id = c.id "
            "WHERE c.user_id = ? GROUP BY c.id ORDER BY c.created_at DESC",
            (USER_ID,),
        ).fetchall()
    return [dict(r) for r in rows]


@app.get("/api/conversations/{conv_id}/messages")
async def get_messages(conv_id: int):
    with closing(db()) as conn:
        conv = conn.execute(
            "SELECT id FROM conversations WHERE id=? AND user_id=?", (conv_id, USER_ID)
        ).fetchone()
        if not conv:
            return JSONResponse({"detail": "对话不存在"}, status_code=404)
        rows = conn.execute(
            "SELECT id, role, content, sources FROM messages WHERE conversation_id=? ORDER BY id",
            (conv_id,),
        ).fetchall()
    return [dict(r) for r in rows]


@app.delete("/api/conversations/{conv_id}")
async def delete_conversation(conv_id: int):
    with closing(db()) as conn, conn:
        conn.execute(
            "DELETE FROM conversations WHERE id=? AND user_id=?", (conv_id, USER_ID)
        )
    return {"ok": True}


# ---------- AI 网关（所有工具统一从这里调 AI） ----------
@app.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    content = ((body or {}).get("content") or "").strip()
    mode = (body or {}).get("mode") or DEFAULT_MODE
    conv_id = (body or {}).get("conversation_id")
    use_kb = bool((body or {}).get("use_kb"))

    if not content:
        return JSONResponse({"detail": "消息不能为空"}, status_code=400)
    if not DEEPSEEK_API_KEY:
        return JSONResponse(
            {"detail": "未配置 DEEPSEEK_API_KEY，请编辑 app/.env 后重启"}, status_code=500
        )

    system = MODES.get(mode, MODES[DEFAULT_MODE])

    # ---------- RAG：先检索个人题库，把相关片段注入提示词 ----------
    sources: list[dict] = []
    kb_block = ""
    if use_kb:
        hits = indexer.search(content, k=4)
        if hits:
            parts = []
            for i, h in enumerate(hits, 1):
                parts.append(f"[{i}] 来源：{h['source']} · {h['title']}\n{h['content']}")
                ref = {"source": h["source"], "title": h["title"]}
                if ref not in sources:
                    sources.append(ref)
            kb_block = (
                "\n\n【用户个人题库资料】以下是检索到的相关片段，回答时优先依据这些资料；"
                "资料中没有的内容可以补充，但要注明是资料之外的扩展。"
                "回答末尾单独一行写明参考来源，格式：「参考：[1][3]」。\n\n"
                + "\n\n".join(parts)
            )
    sources_json = json.dumps(sources, ensure_ascii=False) if sources else ""

    # 落库：新建/校验对话 + 保存用户消息 + 取历史上下文
    conn = db()
    try:
        if not conv_id:
            cur = conn.execute(
                "INSERT INTO conversations(user_id, title, created_at) VALUES(?,?,?)",
                (USER_ID, content[:30], time.time()),
            )
            conv_id = cur.lastrowid
        else:
            row = conn.execute(
                "SELECT id FROM conversations WHERE id=? AND user_id=?", (conv_id, USER_ID)
            ).fetchone()
            if not row:
                return JSONResponse({"detail": "对话不存在"}, status_code=404)
        history = list(
            reversed(
                conn.execute(
                    "SELECT role, content FROM messages WHERE conversation_id=? "
                    "ORDER BY id DESC LIMIT 40",
                    (conv_id,),
                ).fetchall()
            )
        )
        cur = conn.execute(
            "INSERT INTO messages(user_id, conversation_id, role, content, created_at) "
            "VALUES(?,?,?,?,?)",
            (USER_ID, conv_id, "user", content, time.time()),
        )
        user_msg_id = cur.lastrowid
        conn.commit()
    finally:
        conn.close()

    payload_messages = [{"role": "system", "content": system + kb_block}] + [
        dict(r) for r in history
    ] + [{"role": "user", "content": content}]

    async def stream():
        yield f"data: {json.dumps({'conversation_id': conv_id, 'user_msg_id': user_msg_id, 'sources': sources}, ensure_ascii=False)}\n\n"
        full = ""
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(180, connect=10)) as client:
                async with client.stream(
                    "POST",
                    f"{DEEPSEEK_BASE}/chat/completions",
                    headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
                    json={
                        "model": DEEPSEEK_MODEL,
                        "messages": payload_messages,
                        "stream": True,
                        "temperature": 0.7,
                    },
                ) as resp:
                    if resp.status_code != 200:
                        text = (await resp.aread()).decode("utf-8", "ignore")
                        yield f"data: {json.dumps({'error': f'AI 接口返回 {resp.status_code}: {text[:200]}'}, ensure_ascii=False)}\n\n"
                        return
                    async for line in resp.aiter_lines():
                        if not line.startswith("data:"):
                            continue
                        chunk = line[5:].strip()
                        if chunk == "[DONE]":
                            break
                        try:
                            delta = json.loads(chunk)["choices"][0]["delta"].get("content")
                        except Exception:
                            delta = None
                        if delta:
                            full += delta
                            yield f"data: {json.dumps({'content': delta}, ensure_ascii=False)}\n\n"
        except Exception as e:  # 网络/超时等
            yield f"data: {json.dumps({'error': f'请求失败: {e}'}, ensure_ascii=False)}\n\n"
        finally:
            if full:
                with closing(db()) as conn2, conn2:
                    conn2.execute(
                        "INSERT INTO messages(user_id, conversation_id, role, content, created_at, sources) "
                        "VALUES(?,?,?,?,?,?)",
                        (USER_ID, conv_id, "assistant", full, time.time(), sources_json),
                    )
        yield "data: [DONE]\n\n"

    return StreamingResponse(stream(), media_type="text/event-stream")


# ---------- 资料同步（飞书拉取 → 转换 → 重建索引） ----------
_sync_state: dict = {
    "running": False,
    "log": [],
    "steps": [],
    "last_sync": None,
    "last_ok": None,
}
_sync_state_file = DATA_DIR / "sync_state.json"
if _sync_state_file.exists():
    try:
        _sync_state["last_sync"] = json.loads(_sync_state_file.read_text()).get("last_sync")
    except Exception:
        pass


def _run_sync():
    st = _sync_state
    st["running"] = True
    st["log"] = []
    st["steps"] = []
    st["last_ok"] = None

    def log(line: str):
        st["log"].append(line)
        if len(st["log"]) > 500:
            del st["log"][: len(st["log"]) - 500]

    steps = []
    if FEISHU_APP_ID and FEISHU_APP_SECRET:
        cmd = [sys.executable, "tools/feishu_pull.py",
               "--app-id", FEISHU_APP_ID, "--app-secret", FEISHU_APP_SECRET]
        if FEISHU_SPACE_ID:
            cmd += ["--space-id", FEISHU_SPACE_ID]
        steps.append(("拉取飞书文档", cmd))
    else:
        log("· 未配置飞书凭证，跳过拉取（只做转换 + 重建索引）")
    steps.append(("转换 Markdown 入库", [sys.executable, "tools/import_feishu.py"]))
    steps.append(("重建检索索引", [sys.executable, "-m", "app.indexer", "--force"]))

    ok = True
    for name, cmd in steps:
        st["steps"].append({"name": name, "status": "running"})
        log(f"▶ {name}")
        try:
            proc = subprocess.Popen(
                cmd, cwd=str(BASE_DIR),
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, encoding="utf-8", errors="ignore",
                env={**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"},
            )
            for line in proc.stdout:
                line = line.rstrip()
                if line:
                    log(line)
            code = proc.wait()
            if code != 0:
                st["steps"][-1]["status"] = "failed"
                log(f"✗ {name} 失败（退出码 {code}）")
                ok = False
                break
            st["steps"][-1]["status"] = "done"
            log(f"✓ {name} 完成")
        except Exception as e:
            st["steps"][-1]["status"] = "failed"
            log(f"✗ {name} 异常：{e}")
            ok = False
            break

    st["running"] = False
    st["last_ok"] = ok
    if ok:
        st["last_sync"] = time.time()
        try:
            _sync_state_file.write_text(json.dumps({"last_sync": st["last_sync"]}))
            log("✓ 同步完成，题库与索引已更新")
        except Exception as e:
            log(f"· 状态保存失败：{e}")


@app.get("/api/sync/status")
async def sync_status():
    docs = sum(1 for _ in (BASE_DIR / "content").rglob("*.md"))
    chunks = 0
    if indexer.KB_PATH.exists():
        with closing(sqlite3.connect(indexer.KB_PATH)) as conn:
            chunks = conn.execute("SELECT COUNT(*) FROM kb").fetchone()[0]
    return {
        "running": _sync_state["running"],
        "steps": _sync_state["steps"],
        "log": _sync_state["log"][-200:],
        "last_sync": _sync_state["last_sync"],
        "last_ok": _sync_state["last_ok"],
        "feishu_configured": bool(FEISHU_APP_ID and FEISHU_APP_SECRET),
        "stats": {"docs": docs, "chunks": chunks},
    }


@app.post("/api/sync/start")
async def sync_start():
    if _sync_state["running"]:
        return JSONResponse({"detail": "同步正在进行中"}, status_code=409)
    threading.Thread(target=_run_sync, daemon=True).start()
    return {"ok": True}


# ---------- 静态托管（工具） ----------
app.mount("/quiz", StaticFiles(directory=BASE_DIR / "src", html=True), name="quiz")
app.mount("/data", StaticFiles(directory=BASE_DIR / "data"), name="data")
app.mount("/chat", StaticFiles(directory=PLATFORM_DIR / "static" / "chat", html=True), name="chat")
app.mount("/sync", StaticFiles(directory=PLATFORM_DIR / "static" / "sync", html=True), name="sync")


if __name__ == "__main__":
    import uvicorn

    print(f"平台已启动: http://127.0.0.1:{PORT}/")
    uvicorn.run(app, host="127.0.0.1", port=PORT)
