# -*- coding: utf-8 -*-
"""video_digest — B站视频转"可学习素材"流水线

输入B站视频链接，自动产出：
  info.json    视频/UP主信息
  字幕.md      CC字幕（若B站提供，零成本）或 faster-whisper 本地转写
  关键帧/*.jpg 按固定间隔抽取的画面帧（股票视频的画面主体是K线图）
  视频.mp4 / 音频.wav（中间产物，可删）

用法:
  python video_digest.py <链接或BV号>              # 全流程
  python video_digest.py <链接> --seconds 120      # 只处理前120秒（快速验证）
  python video_digest.py <链接> --model base       # 更快的转写模型（默认 small）
  python video_digest.py <链接> --fps 0.2          # 每5秒一帧（默认每3秒）
  python video_digest.py <链接> --no-video         # 只拉信息+字幕，不下载

依赖: pip install yt-dlp faster-whisper imageio-ffmpeg
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = Path(__file__).parent
# B站未登录只能试看30秒，需从已登录的浏览器读取 Cookie: edge / chrome / firefox
COOKIE_BROWSER = "edge"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def log(msg):
    print(msg, flush=True)


def get_ffmpeg():
    """项目自带的 ffmpeg/ffprobe（bin/），并加入 PATH 供 yt-dlp 探测。"""
    bin_dir = HERE / "bin"
    if not (bin_dir / "ffmpeg.exe").exists():
        import imageio_ffmpeg
        bin_dir.mkdir(exist_ok=True)
        shutil.copy(imageio_ffmpeg.get_ffmpeg_exe(), bin_dir / "ffmpeg.exe")
    os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ.get("PATH", "")
    return str(bin_dir / "ffmpeg.exe")


def http_json(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def extract_bvid(text):
    m = re.search(r"(BV[0-9A-Za-z]{10})", text)
    if not m:
        raise SystemExit("无法从输入中解析 BV 号: %s" % text)
    return m.group(1)


def fetch_info(bvid):
    js = http_json(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}")
    if js.get("code") != 0:
        raise SystemExit("拉取视频信息失败: %s" % js.get("message"))
    d = js["data"]
    return {
        "bvid": bvid,
        "title": d["title"],
        "desc": d["desc"],
        "owner": d["owner"]["name"],
        "duration": d["duration"],
        "view": d["stat"]["view"],
        "pubdate": d["pubdate"],
        "pages": [{"cid": p["cid"], "part": p["part"]} for p in d.get("pages", [])],
        "url": f"https://www.bilibili.com/video/{bvid}",
    }


def try_fetch_cc_subtitle(info, out_dir):
    """尝试拉B站CC字幕（大多需登录，拿不到返回 None）。"""
    import requests
    for page in (info["pages"] or [{"cid": None}]):
        cid = page["cid"]
        if not cid:
            continue
        for api in ("https://api.bilibili.com/x/player/wbi/v2",
                    "https://api.bilibili.com/x/player/v2"):
            try:
                r = requests.get(api, params={"bvid": info["bvid"], "cid": cid},
                                 headers={"User-Agent": UA, "Referer": "https://www.bilibili.com"},
                                 timeout=15)
                subs = ((r.json().get("data") or {}).get("subtitle") or {}).get("subtitles") or []
                if not subs:
                    continue
                sub_url = subs[0].get("subtitle_url", "")
                if sub_url.startswith("//"):
                    sub_url = "https:" + sub_url
                body = http_json(sub_url)
                lines = [(b["from"], b["to"], b["content"]) for b in body.get("body", [])]
                if lines:
                    md = out_dir / "字幕.md"
                    with open(md, "w", encoding="utf-8") as f:
                        f.write(f"# {info['title']}（CC字幕）\n\n")
                        for a, b_, c in lines:
                            f.write(f"[{int(a//60):02d}:{int(a%60):02d}] {c}\n")
                    return md
            except Exception as e:
                log(f"  CC字幕尝试失败（{api.split('/')[-2]}/{e.__class__.__name__}），继续")
    return None


def download_video(info, out_dir, seconds=None):
    import yt_dlp
    target = out_dir / "视频.mp4"
    if target.exists() and not target.with_suffix(".part").exists() and target.stat().st_size > 0:
        # 完整性粗校验：能用 ffprobe 读出时长且接近预期才视为已下载
        try:
            r = subprocess.run([get_ffmpeg().replace("ffmpeg.exe", "ffprobe.exe"), "-v", "error",
                                "-show_entries", "format=duration", "-of", "json",
                                str(target)], check=True, capture_output=True, text=True)
            dur = float(json.loads(r.stdout)["format"]["duration"])
            expect = info.get("duration") or 0
            if seconds or expect == 0 or dur >= expect * 0.9:
                log(f"  视频已存在（{dur:.0f}s），跳过下载")
                return target
            log(f"  视频不完整（{dur:.0f}s/{expect}s），重新下载")
        except Exception:
            log("  视频校验失败，重新下载")
        target.unlink()
    ffmpeg = get_ffmpeg()
    fmt = ("bv*[height<=480][ext=mp4]+ba[ext=m4a]/b[height<=480][ext=mp4]/"
           "bv*[height<=480]+ba/b")
    opts = {
        "format": fmt,
        "outtmpl": str(target),
        "ffmpeg_location": ffmpeg,
        "merge_output_format": "mp4",
        "retries": 3,
        "noprogress": True,
        "quiet": True,
        "no_warnings": True,
    }
    cookie_file = HERE / "cookies.txt"
    if cookie_file.exists():
        opts["cookiefile"] = str(cookie_file)
    elif COOKIE_BROWSER:
        opts["cookiesfrombrowser"] = (COOKIE_BROWSER,)
    if seconds:
        opts["download_ranges"] = lambda _info, _ydl: [{"start_time": 0, "end_time": seconds}]
        opts["force_keyframes_at_cuts"] = True
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([info["url"]])
    if not target.exists():
        raise SystemExit("下载失败")
    return target


def extract_audio(video, out_dir, ffmpeg):
    wav = out_dir / "音频.wav"
    if wav.exists():
        return wav
    subprocess.run([ffmpeg, "-y", "-i", str(video), "-vn", "-ac", "1", "-ar", "16000",
                    str(wav)], check=True, capture_output=True)
    return wav


def transcribe(wav, out_dir, info, model_size, ffmpeg):
    md = out_dir / "字幕.md"
    if md.exists() and md.stat().st_size > 100:
        log("  文字稿已存在，跳过转写")
        return md
    # 用 ffmpeg 解码为 16kHz float32 原始 PCM，绕开 PyAV 版本兼容问题
    import numpy as np
    raw = out_dir / "_audio16k.raw"
    subprocess.run([ffmpeg, "-y", "-i", str(wav), "-ac", "1", "-ar", "16000",
                    "-f", "f32le", str(raw)], check=True, capture_output=True)
    audio = np.frombuffer(raw.read_bytes(), dtype=np.float32)
    raw.unlink()
    from faster_whisper import WhisperModel
    log(f"  加载 whisper 模型 {model_size}（首次会自动下载，中文建议 small 及以上）")
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, _info = model.transcribe(audio, language="zh", vad_filter=True,
                                       beam_size=5)
    # 逐段即时落盘：中途崩溃也保留已转写进度（空文件/短文件下次会重试而非跳过）
    with open(md, "w", encoding="utf-8") as f:
        f.write(f"# {info['title']}（whisper {model_size} 转写）\n\n")
        n = 0
        for seg in segments:
            f.write(f"[{int(seg.start//60):02d}:{int(seg.start%60):02d}] {seg.text.strip()}\n")
            f.flush()
            n += 1
    log(f"  转写完成：{n} 段")
    return md


def extract_frames(video, out_dir, fps, ffmpeg):
    frames = out_dir / "关键帧"
    frames.mkdir(exist_ok=True)
    if any(frames.iterdir()):
        log("  关键帧已存在，跳过抽帧")
        return frames
    subprocess.run([ffmpeg, "-y", "-i", str(video), "-vf",
                    f"fps={fps},scale=1280:-1", str(frames / "帧_%03d.jpg")],
                   check=True, capture_output=True)
    return frames


def main():
    ap = argparse.ArgumentParser(description="B站视频 → 字幕+关键帧 学习素材")
    ap.add_argument("url", help="B站视频链接或BV号")
    ap.add_argument("--seconds", type=int, default=None, help="只处理前N秒（测试用）")
    ap.add_argument("--model", default="small", help="whisper 模型: tiny/base/small/medium")
    ap.add_argument("--fps", default="1/3", help="抽帧频率，默认每3秒一帧（1/3）")
    ap.add_argument("--no-video", action="store_true", help="只拉信息与CC字幕，不下载")
    args = ap.parse_args()

    bvid = extract_bvid(args.url)
    log(f"[1/5] 拉取视频信息 {bvid}")
    info = fetch_info(bvid)
    log(f"  《{info['title']}》 UP主: {info['owner']} 时长: {info['duration']}秒 播放: {info['view']}")

    slug = re.sub(r'[\\/:*?"<>|]', "_", info["title"])[:40] or bvid
    out_dir = HERE / "output" / f"{slug}_{bvid}"
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    log("[2/5] 尝试拉取CC字幕（免转写）")
    sub = try_fetch_cc_subtitle(info, out_dir)
    if sub:
        log(f"  拿到CC字幕: {sub.name}")

    ffmpeg = get_ffmpeg()
    video = None
    if not args.no_video:
        log("[3/5] 下载视频（≤480P）")
        video = download_video(info, out_dir, args.seconds)
        log(f"  已下载: {video.name} ({video.stat().st_size/1e6:.1f}MB)")

        if not sub:
            log("[4/5] 本地语音转写（faster-whisper）")
            wav = extract_audio(video, out_dir, ffmpeg)
            sub = transcribe(wav, out_dir, info, args.model, ffmpeg)
            log(f"  文字稿: {sub.name}")
        else:
            log("[4/5] 已有CC字幕，跳过转写")

        log(f"[5/5] 抽取关键帧（fps={args.fps}）")
        frames = extract_frames(video, out_dir, args.fps, ffmpeg)
        log(f"  关键帧: {len(list(frames.glob('*.jpg')))} 张 → {frames}")
    else:
        log("[3/5] --no-video，跳过下载/转写/抽帧")

    log("\n完成。产出目录: " + str(out_dir))
    for p in sorted(out_dir.rglob("*")):
        if p.is_file():
            log(f"  {p.relative_to(out_dir)}  ({p.stat().st_size/1e3:.0f} KB)")


if __name__ == "__main__":
    main()
