# 面试题库 · 飞书资料整理工程

把飞书知识库里的上百篇面试文档，变成**一个能考你、帮你记住的自测工具**。

## 流程总览

```
飞书知识库 ──导出──> feishu_export/ ──脚本转换──> content/*.md ──抽取──> data/quiz-data.js ──> 打开 src/index.html 开始刷题
```

## 第一步：从飞书把资料弄出来

> 优先试方式一：一次搞定整个知识库，最适合上百篇的规模。

### 方式零：API 批量拉取（已写好脚本，推荐）

不需要逐篇点导出，也不用找管理员：

1. 打开 https://open.feishu.cn → 开发者后台 → 创建**企业自建应用**
2. 「权限管理」开通：`wiki:wiki:readonly`、`docx:document:readonly`、`drive:drive:readonly`（按名称搜索勾选）
3. 创建版本并发布（管理员审批通过后生效）
4. 「凭证与基础信息」页拿到 App ID / App Secret，然后：

```powershell
# 第一次跑：列出你有权限的知识库
python tools/feishu_pull.py --app-id xxx --app-secret xxx

# 拉整个知识库（保留目录结构）
python tools/feishu_pull.py --app-id xxx --app-secret xxx --space-id 7003xxxxxxxx

# 文档在云空间文件夹里的话
python tools/feishu_pull.py --app-id xxx --app-secret xxx --folder-token fldcnxxxxxx
```

拉完直接跑 `python tools/import_feishu.py` 即可。

> 注意：知识库需要在「知识库设置 → 添加文档应用」里把你的应用加为协作者，否则 API 看不到里面的文档。Secret 只在本机命令行使用，不要提交到代码仓库。

### 方式一：知识库批量导出（需要管理员）

1. 打开飞书（桌面端或网页版），进入你的**知识库**
2. 右上角 `···` / 设置 → 找 **「导出知识库」**（部分版本在「知识库设置 → 导出」）
3. 选择导出格式为 **HTML**（比 Word 更好解析），等待打包完成
4. 下载 zip，**不用解压**，整个 zip 直接丢进 `feishu_export/`

> 没有这个按钮？通常是权限限制（需要知识库管理员）。找空间管理员导出，或退到方式二/三。

### 方式二：逐个文档导出 Markdown

打开文档 → 右上角 `···` → **导出 / 下载为** → **Markdown** → 下载。

上百篇手点很痛苦，两种减负办法：
- 只导高频目录（按知识库一级目录分批处理）
- 让我用浏览器自动化帮你批量点：你先登录好飞书，把知识库链接给我

### 方式三：飞书开放平台 API（有开发者权限时）

创建企业自建应用，开通 `docx:document:readonly` / `wiki:node:retrieve` / `drive:file:export` 权限后：

| 用途 | 接口 |
|---|---|
| 列出知识库全部节点 | `GET /open-apis/wiki/v2/spaces/{space_id}/nodes` |
| 取节点树 | `POST /open-apis/wiki/v2/spaces/get_node` |
| 读文档正文块 | `GET /open-apis/docx/v1/documents/{doc_id}/blocks` |
| 导出成文件 | `POST /open-apis/drive/v1/files/export` |

如果你有 `app_id` / `app_secret`，告诉我，我直接写拉取脚本。

## 第二步：转换 + 抽题

```powershell
# 装一次依赖（可选，装了解析质量更好）
pip install -r tools/requirements.txt

# 转换（自动解压 zip、转 Markdown、抽取问答卡）
python tools/import_feishu.py

# 只看会生成什么，不写文件
python tools/import_feishu.py --dry-run
```

产物：
- `content/` — 规范化后的 Markdown，保留原目录结构
- `data/quiz-data.js` — 题库数据（页面直接读取）

### 问答抽取规则

脚本按优先级识别三种结构：

1. **显式问答**：`Q:` / `问：` / `问题：` 与 `A:` / `答：` / `答案：` 配对
2. **标题即问题**：`### xxx` 当作问题，其下正文当作答案
3. **兜底要点卡**：没命中上面两种时，用「标题路径」当问题、该节要点当答案

分类默认取文件所在的一级目录名（如 `Java/并发/xxx.md` → 分类 `Java`）。

## 第三步：开始自测

双击打开 `src/index.html`（纯静态，无需起服务）。

- **复习**：先出题，自己答，再翻答案，三档自评（忘了 / 模糊 / 掌握）
- **间隔重复**：基于 Leitner 盒子，答得好出现频率自动降低，记不牢的反复出现
- **浏览**：搜索 / 按分类查看全部题目
- **统计**：掌握率、各分类进度、待复习数量
- **编辑**：卡片内容可以直接改，覆盖保存在浏览器本地（不影响原始文件）

快捷键：`空格` 翻答案 / 下一题，`1 2 3` 自评，`E` 编辑。

## 目录说明

```
feishu_export/   放飞书导出的原始 zip 或文件（你只需要动这里）
content/         转换后的 Markdown（脚本生成）
data/            题库数据（脚本生成）
src/             自测页面（双击 index.html 打开）
tools/           转换与抽取脚本
```

## 想更进一步

资料灌进来之后，还可以让我做：
- 按主题重新归类、跨文档去重合并
- 提炼一份「高频考点速记清单」
- 导出成 Word / PDF 便于打印背诵
- 做成可搜索的静态知识库站点
