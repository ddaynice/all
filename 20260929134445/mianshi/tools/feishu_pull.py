# -*- coding: utf-8 -*-
"""
通过飞书开放平台 API，把整个知识库 / 云空间文件夹批量拉取为 Markdown。

准备工作（一次性）：
  1. 打开 https://open.feishu.cn → 开发者后台 → 创建「企业自建应用」
  2. 在「权限管理」开通这些权限（复制权限名搜索即可）：
       - docx:document:readonly      查看新版文档
       - drive:drive:readonly        查看、评论和下载云空间中所有文件
       - wiki:wiki:readonly          查看知识库
       - drive:drive.export          导出云文档（备用）
  3. 创建应用版本并发布（企业管理员审批通过后权限才生效；
     如果你自己就是管理员，直接通过即可）
  4. 在「凭证与基础信息」页拿到 App ID 和 App Secret

用法：
  # 推荐：以「你本人」身份授权（个人版知识库用这个，不需要给应用加协作者）
  #   先去开发者后台 -> 你的应用 -> 安全设置 -> 重定向 URL 添加: http://localhost:3123/callback
  python tools/feishu_pull.py --app-id xxx --app-secret xxx --user

  # 应用身份（需要知识库把应用加为协作者，个人版往往做不到）
  python tools/feishu_pull.py --app-id xxx --app-secret xxx            # 列出可访问的知识库
  python tools/feishu_pull.py --app-id xxx --app-secret xxx --space-id 7003xxxxxxxx
  python tools/feishu_pull.py --app-id xxx --app-secret xxx --folder-token fldcnxxxxxx
  # 也可以用环境变量 FEISHU_APP_ID / FEISHU_APP_SECRET 代替命令行参数

导出结果落在 feishu_export/api/，之后直接跑：
  python tools/import_feishu.py
"""
from __future__ import annotations

import argparse
import http.server
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

API = "https://open.feishu.cn/open-apis"
ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "feishu_export" / "api"
SLEEP = 0.15  # 简单限速，避免触发频控

PERMISSION_HINT = (
    "\n[提示] 没有权限或返回错误时，请检查：\n"
    "  1) 应用是否已发布且管理员审批通过\n"
    "  2) 是否开通 wiki:wiki:readonly / docx:document:readonly / drive:drive:readonly\n"
    "  3) 知识库是否已把这个应用添加为协作者（知识库设置 -> 添加文档应用）\n"
)


def http_json(method, path, token=None, data=None, params=None):
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    body = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            return json.loads(e.read().decode("utf-8"))
        except Exception:
            return {"code": e.code, "msg": str(e)}


def get_token(app_id, app_secret):
    r = http_json("POST", "/auth/v3/tenant_access_token/internal",
                  data={"app_id": app_id, "app_secret": app_secret})
    if r.get("code") != 0:
        print(f"[失败] 获取 tenant_access_token: {r.get('code')} {r.get('msg')}")
        print(PERMISSION_HINT)
        sys.exit(1)
    return r["tenant_access_token"]


def get_user_token(app_id, app_secret, port=3123):
    """OAuth 授权码流程：浏览器登录 -> 本地回调拿 code -> 换 user_access_token。"""
    redirect_uri = f"http://localhost:{port}/callback"
    scope = "wiki:wiki:readonly docx:document:readonly drive:drive:readonly"
    auth_url = ("https://accounts.feishu.cn/open-apis/authen/v1/authorize?"
                + urllib.parse.urlencode({"app_id": app_id, "redirect_uri": redirect_uri,
                                          "scope": scope, "state": "quiz"}))
    print("正在打开浏览器授权页…请登录飞书并点击「同意/授权」。")
    print(f"（如果没有自动打开，手动访问：{auth_url}）\n")
    webbrowser.open(auth_url)

    holder = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            qs = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            holder["code"] = (qs.get("code") or [""])[0]
            holder["err"] = (qs.get("error") or [""])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            msg = "授权成功，可以关闭这个页面回到终端。" if holder["code"] \
                else "授权失败：" + holder["err"]
            self.wfile.write(f"<h3>{msg}</h3>".encode("utf-8"))

        def log_message(self, *args):
            pass

    server = http.server.HTTPServer(("localhost", port), Handler)
    server.handle_request()
    server.server_close()

    code = holder.get("code")
    if not code:
        print("[失败] 没有拿到授权 code：", holder.get("err") or "回调为空")
        print(f"请确认开发者后台 -> 安全设置 -> 重定向 URL 里有：{redirect_uri}")
        sys.exit(1)

    r = http_json("POST", "/authen/v2/oauth/token", data={
        "grant_type": "authorization_code",
        "client_id": app_id,
        "client_secret": app_secret,
        "code": code,
        "redirect_uri": redirect_uri,
    })
    access = (r.get("data") or {}).get("access_token") or r.get("access_token")
    if not access:
        print("[失败] 换取 user_access_token 失败：")
        print(json.dumps(r, ensure_ascii=False)[:800])
        sys.exit(1)
    return access


def paged(path, token, params=None, key="items"):
    params = dict(params or {})
    params["page_size"] = 50
    out = []
    while True:
        r = http_json("GET", path, token, params=params)
        if r.get("code") != 0:
            print(f"[失败] {path}: {r.get('code')} {r.get('msg')}")
            print(PERMISSION_HINT)
            sys.exit(1)
        data = r.get("data", {})
        out += data.get(key) or []
        if not data.get("has_more"):
            return out
        params["page_token"] = data.get("page_token")
        time.sleep(SLEEP)


def safe_name(name):
    name = re.sub(r'[\\/:*?"<>|\n\r\t]', "_", name or "").strip()
    return name[:80] or "untitled"


# ---------------------------------------------------------------------------
# 文档 -> Markdown
# ---------------------------------------------------------------------------
def elements_md(elements):
    out = []
    for el in elements or []:
        tr = el.get("text_run")
        if not tr:
            continue
        c = tr.get("content", "")
        style = tr.get("text_element_style") or {}
        if style.get("inline_code"):
            c = "`%s`" % c
        if style.get("bold"):
            c = "**%s**" % c
        if style.get("italic"):
            c = "*%s*" % c
        if style.get("strikethrough"):
            c = "~~%s~~" % c
        link = style.get("link") or {}
        if link.get("url"):
            c = "[%s](%s)" % (c, urllib.parse.unquote(link["url"]))
        out.append(c)
    return "".join(out)


def table_md(block, idmap):
    tbl = block.get("table", {}) or {}
    prop = tbl.get("property", {}) or {}
    rows, cols = prop.get("row_size", 0), prop.get("column_size", 0)
    cells = tbl.get("cells", [])
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            cb = idmap.get(cells[i * cols + j]) if i * cols + j < len(cells) else None
            text = cell_text(cb, idmap)
            row.append(text.replace("\n", " ").replace("|", "\\|") or " ")
        grid.append(row)
    if not grid:
        return ""
    lines = ["| " + " | ".join(grid[0]) + " |",
             "| " + " | ".join(["---"] * cols) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in grid[1:]]
    return "\n".join(lines)


def cell_text(cell_block, idmap):
    parts = []
    for cid in cell_block.get("children", []):
        b = idmap.get(cid)
        if not b:
            continue
        if b.get("block_type") == 2:
            parts.append(elements_md(b.get("text", {}).get("elements")))
    return " ".join(p for p in parts if p)


def blocks_to_md(items):
    idmap = {b["block_id"]: b for b in items}
    root = next((b for b in items if b.get("block_type") == 1), None)
    lines = []

    def walk(bid, depth):
        b = idmap.get(bid)
        if not b:
            return
        t = b.get("block_type")
        md = None
        if 2 <= t <= 8:  # text / heading1..6
            keys = {2: "text", 3: "heading1", 4: "heading2", 5: "heading3",
                    6: "heading4", 7: "heading5", 8: "heading6"}
            content = elements_md(b.get(keys[t], {}).get("elements"))
            if content:
                md = ("#" * (t - 1) if t >= 3 else "") + (content if t == 2 else " " + content)
                if t >= 3:
                    md = "#" * (t - 1) + " " + content
        elif t == 9:  # bullet
            md = "  " * depth + "- " + elements_md(b.get("bullet", {}).get("elements"))
        elif t == 10:  # ordered
            md = "  " * depth + "1. " + elements_md(b.get("ordered", {}).get("elements"))
        elif t == 11:  # code
            content = elements_md(b.get("code", {}).get("elements"))
            lang = ((b.get("code", {}) or {}).get("style") or {}).get("language") or ""
            md = "```%s\n%s\n```" % (lang, content)
        elif t == 12:  # quote
            md = "> " + elements_md(b.get("quote", {}).get("elements"))
        elif t == 14:  # todo
            done = ((b.get("todo", {}) or {}).get("style") or {}).get("done")
            md = "- [%s] %s" % ("x" if done else " ",
                                elements_md(b.get("todo", {}).get("elements")))
        elif t == 19:  # divider
            md = "---"
        elif t == 28:  # table
            md = table_md(b, idmap)
        if md:
            lines.append(md)
            lines.append("")
        for c in b.get("children", []):
            walk(c, depth + 1 if t in (9, 10) else depth)

    if root:
        for c in root.get("children", []):
            walk(c, 0)
    else:  # 没有 page 根块时按顺序兜底
        for b in items:
            if b.get("block_type") == 2:
                lines.append(elements_md(b.get("text", {}).get("elements")))
    return "\n".join(lines).strip()


def fetch_doc_md(token, document_id, title):
    items = paged(f"/docx/v1/documents/{document_id}/blocks", token, key="items")
    if items:
        md = blocks_to_md(items)
        if md:
            return md
    # 兜底：纯文本接口（无格式，但保底有内容）
    r = http_json("GET", f"/docx/v1/documents/{document_id}/raw_content", token)
    if r.get("code") == 0:
        return r["data"].get("content", "").strip()
    print(f"  [失败] {title}: {r.get('code')} {r.get('msg')}")
    return ""


# ---------------------------------------------------------------------------
# 遍历
# ---------------------------------------------------------------------------
def list_wiki_spaces(token):
    items = paged("/wiki/v2/spaces", token)
    for s in items:
        print(f"  space_id={s['space_id']}  {s.get('name', '')}")
    print("\n选定后加参数: --space-id <space_id>")


def pull_wiki(token, space_id):
    print(f"拉取知识库 {space_id} ...")
    stack = [("", OUT_DIR)]
    n_ok = n_skip = 0
    while stack:
        parent, folder = stack.pop()
        nodes = paged(f"/wiki/v2/spaces/{space_id}/nodes", token,
                      params={"parent_node_token": parent} if parent else None)
        for node in nodes:
            title = safe_name(node.get("title"))
            path = folder / title
            if node.get("has_child"):
                stack.append((node["node_token"], path))
            otype = node.get("obj_type")
            if otype in ("docx", "doc"):
                path.parent.mkdir(parents=True, exist_ok=True)
                md = fetch_doc_md(token, node["obj_token"], title)
                path.with_suffix(".md").write_text(md or f"> [{title}] 拉取失败", encoding="utf-8")
                n_ok += 1
                print(f"  [ok] {'/'.join(path.relative_to(OUT_DIR).parts[:-1]) or '.'}/{title}")
            else:
                n_skip += 1
                print(f"  [跳过] {title} ({otype})")
            time.sleep(SLEEP)
    print(f"\n完成：成功 {n_ok} 篇，跳过 {n_skip} 个（非文档类型）")
    print(f"输出目录: {OUT_DIR}")


def pull_folder(token, folder_token):
    print(f"拉取云空间文件夹 {folder_token} ...")
    stack = [(folder_token, OUT_DIR)]
    n_ok = n_skip = 0
    while stack:
        ft, folder = stack.pop()
        files = paged("/drive/v1/files", token, params={"folder_token": ft}, key="files")
        for f in files:
            ftype = f.get("type")
            name = safe_name(f.get("name"))
            path = folder / name
            if ftype == "folder":
                stack.append((f["token"], path))
            elif ftype in ("docx", "doc"):
                path.parent.mkdir(parents=True, exist_ok=True)
                md = fetch_doc_md(token, f["token"], name)
                path.with_suffix(".md").write_text(md or f"> [{name}] 拉取失败", encoding="utf-8")
                n_ok += 1
                print(f"  [ok] {name}")
            else:
                n_skip += 1
                print(f"  [跳过] {name} ({ftype})")
            time.sleep(SLEEP)
    print(f"\n完成：成功 {n_ok} 篇，跳过 {n_skip} 个")
    print(f"输出目录: {OUT_DIR}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app-id", default=os.environ.get("FEISHU_APP_ID"))
    ap.add_argument("--app-secret", default=os.environ.get("FEISHU_APP_SECRET"))
    ap.add_argument("--user", action="store_true",
                    help="以你本人身份授权（个人版知识库推荐）")
    ap.add_argument("--port", type=int, default=3123, help="OAuth 本地回调端口")
    ap.add_argument("--space-id", help="知识库 space_id（不传则列出所有知识库）")
    ap.add_argument("--folder-token", help="云空间文件夹 token")
    args = ap.parse_args()

    if not args.app_id or not args.app_secret:
        ap.error("需要 --app-id / --app-secret（或环境变量 FEISHU_APP_ID / FEISHU_APP_SECRET）")

    if args.user:
        token = get_user_token(args.app_id, args.app_secret, args.port)
        print("[ok] 已拿到你的授权\n")
    else:
        token = get_token(args.app_id, args.app_secret)
        print("[ok] 认证成功\n")

    if args.space_id:
        pull_wiki(token, args.space_id)
    elif args.folder_token:
        pull_folder(token, args.folder_token)
    else:
        print("你有权限的知识库：")
        list_wiki_spaces(token)
        print("\n云空间文件夹：把浏览器里文件夹链接末尾的 token 传给 --folder-token")


if __name__ == "__main__":
    main()
