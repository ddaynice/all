# -*- coding: utf-8 -*-
"""拉取UP主视频列表（B站 wbi 签名接口）。用法: python list_videos.py <mid> [页数]"""
import json
import sys
import urllib.request
from functools import reduce

MIXIN = [46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49,
         33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40,
         61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11,
         36, 20, 34, 44, 52]
UA = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"),
      "Referer": "https://space.bilibili.com/25270495/video",
      "Origin": "https://space.bilibili.com",
      "Accept": "application/json, text/plain, */*",
      "Accept-Language": "zh-CN,zh;q=0.9"}


def get_cookies():
    spi = http_json("https://api.bilibili.com/x/frontend/finger/spi")
    d = spi.get("data") or {}
    ck = f"buvid3={d.get('b_3','')}; buvid4={d.get('b_4','')}"
    # 附带本地 cookies.txt 里的 SESSDATA（若有）
    from pathlib import Path
    f = Path(__file__).parent / "cookies.txt"
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            if "\tSESSDATA\t" in line:
                ck += "; SESSDATA=" + line.split("\tSESSDATA\t")[-1].strip()
                break
    return ck


def http_json(url, cookie=None):
    headers = dict(UA)
    if cookie:
        headers["Cookie"] = cookie
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def wbi_sign(params):
    nav = http_json("https://api.bilibili.com/x/web-interface/nav")
    wbi = nav["data"]["wbi_img"]
    img_key = wbi["img_url"].rstrip(".png").rsplit("/", 1)[-1].replace(".png", "")
    sub_key = wbi["sub_url"].rstrip(".png").rsplit("/", 1)[-1].replace(".png", "")
    raw = img_key + sub_key
    key = "".join(raw[i] for i in MIXIN)[:32]
    params = dict(params, wts=0)
    params["wts"] = __import__("time").time().__int__()
    query = "&".join(f"{k}={v}" for k, v in
                     sorted(params.items(), key=lambda x: x[0]))
    import hashlib
    params["w_rid"] = hashlib.md5((query + key).encode()).hexdigest()
    return params


def main(mid, pages=3):
    cookie = get_cookies()
    seen = {}
    for pn in range(1, pages + 1):
        params = wbi_sign({"mid": mid, "ps": 30, "pn": pn, "order": "pubdate"})
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        js = http_json(f"https://api.bilibili.com/x/space/wbi/arc/search?{qs}", cookie)
        vlist = (js.get("data") or {}).get("list", {}).get("vlist", [])
        if not vlist:
            print(f"-- 第{pn}页为空: code={js.get('code')} {js.get('message')}")
            break
        for v in vlist:
            seen[v["bvid"]] = (v["created"] if "created" in v else v.get("pubdate", 0),
                               v["title"], v["length"], v["play"])
    import time
    for bvid, (ts, title, length, play) in sorted(seen.items(), key=lambda x: -x[1][0]):
        print(f"{time.strftime('%m-%d', time.localtime(ts))} {bvid} {length:>8} {play:>8} {title[:45]}")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3)
