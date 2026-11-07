# ManShi 项目集

本仓库包含三个部分：K线形态相似度扫描工具、B站视频学习流水线、面试资料。

---

## 一、pattern-scan — K线形态相似度扫描工具

把最近 N 根K线的形状作为查询片段，在全部历史数据中检索最相似的历史片段（DTW 动态时间规整），
并统计它们后续走势的分布（上涨概率、价位带分位、转折时点、分水岭三件套等）。
灵感来自 BOSS墨 手工"搬历史走势对照"的方法论，工具化 + 量化。

### 快速开始

双击 **`pattern-scan/一键启动.pyw`** → 自动启动后台服务并打开浏览器界面。
（注意：不要直接双击 index.html，file:// 协议无法与后台通信。）

### 主要功能

- **多数据源自动切换**：A股（东财→腾讯）、期货（新浪主力连续，如 AU0 黄金 / AG0 白银），
  支持 4小时 / 日线 / 周线
- **起点归一化 + DTW**：只比形状不比量级，比欧氏距离更接近人眼判断
- **相似片段可视化**：半透明蜡烛叠加 + 手动时序/价位偏移对齐 + 滚轮缩放/平移
- **分水岭统计**（BOSS墨体系）：
  - 自动识别前高/前低水平线，判定当前状态（站上前高=洗盘确认 / 跌破前低=等反弹处理）
  - 相似窗口池的"站上前高概率/用时"、"跌破前低概率、破位深度、反弹幅度"（大跌大弹）、
    "止跌确认（连续5根不创新低）时点与止跌后涨幅"
- **转折时点统计**：相似样本后续首次创新高 / 首次破位的时点分布
- **价位带分位统计**：后续路径的 25/50/75 分位（入场区间测算依据）

### 命令行用法

```powershell
cd pattern-scan
python pattern_scan.py --market futures --symbol AU0            # 黄金主力连续
python pattern_scan.py --market stock  --symbol 600519          # 贵州茅台
python pattern_scan.py --market futures --symbol AU0 --tf weekly --window 40 --horizon 30
```

输出：`output/<品种>_scan.png`（对比图）+ `output/<品种>_report.md`（统计报告）。

### 测试

```powershell
python test_api.py    # API 14 用例
python test_ui.py     # 浏览器 UI 回归
```

### 目录结构

```
pattern-scan/
├── pattern_scan.py    # 核心逻辑：数据获取 + DTW 扫描 + 分水岭/转折统计 + 报告绘图
├── webapp.py          # Flask 后端（/api/scan），数据缓存
├── static/index.html  # Web 前端（KLineChart 本地内置，无 CDN 依赖）
├── test_*.py          # API / UI / 拖拽测试
└── 一键启动.pyw        # 双击启动：自动拉起服务 + 打开浏览器
```

---

## 二、video-digest — B站视频学习流水线

输入B站视频链接，自动产出可学习的素材（字幕文字稿 + 关键帧），配合 AI 通读提炼
博主的方法论与交易系统（已提炼：BOSS墨交易系统，见 `BOSS墨交易系统.md`）。

### 用法

```powershell
cd video-digest
python video_digest.py <B站链接或BV号>              # 全流程
python video_digest.py <链接> --seconds 120         # 只处理前2分钟（快速验证）
python video_digest.py <链接> --model medium        # 更准的转写模型（默认 small）
python video_digest.py <链接> --no-video            # 只拉信息与CC字幕
python list_videos.py <mid>                         # 拉取UP主视频列表（需 wbi 签名，偶被限流）
```

### 产出（`output/标题_BV号/`）

- `字幕.md` — 优先B站CC字幕（免转写），否则 faster-whisper 本地转写（带时间戳）
- `关键帧/*.jpg` — 每 3 秒一帧的画面截图
- `info.json` — 标题 / UP主 / 简介 / 时长
- `方法论提炼.md` — 人工/AI 通读素材后的方法论整理

### 依赖

`pip install yt-dlp faster-whisper imageio-ffmpeg`，`bin/` 内含完整 ffmpeg（含 ffprobe）。

### 安全提醒

`cookies.txt` 存有B站登录凭证（SESSDATA，未登录只能试看30秒，必须登录才能拉完整视频）。
**该文件已被 .gitignore 排除，严禁上传或分享**；在B站退出登录会使其自动失效。

---

## 三、20260929134445 — 面试资料

约 200 个文件（markdown / pdf / py），整理的学习与面试素材，与本仓库两个工具项目无关。

---

## 更新记录

- pattern-scan：分水岭三件套统计（站上前高/大跌大弹/止跌确认）、KLineChart 重构
  （真实价格轴、画图工具基础、无缓存页面）、一键启动器
- video-digest：CC字幕→whisper 转写回退、断点续传、嵌套仓库清理、UP主列表拉取

## 免责声明

所有统计结果基于历史形态相似度，**相似不等于因果**，不构成任何投资建议。
