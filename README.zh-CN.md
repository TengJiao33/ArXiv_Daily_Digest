# ArXiv_Daily_Digest

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
![Dashboard](https://img.shields.io/badge/Dashboard-Static%20HTML%20%2B%20Local%20API-2f7d62)
![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

[English](README.md)

ArXiv_Daily_Digest 是一个面向研究论文采集、补全、存储与审阅的可配置流水线。系统基于预定义研究方向执行 arXiv 检索、可选引用扩展、元数据补全、结构化抽取、Markdown 产物生成与静态 Dashboard 展示。

当前仓库内置 Agent Reliability Radar 配置。项目实现以方向配置为核心组织单元，可按需要调整为其他研究范围。

## 功能

| 模块 | 说明 |
| --- | --- |
| 论文采集 | 按方向级查询条件从 arXiv 获取候选论文。 |
| 引用扩展 | 基于种子论文通过 Semantic Scholar 扩展候选集合。 |
| 相关性过滤 | 按可配置关键词与主题条件筛选候选论文。 |
| 元数据补全 | 补全代码仓库、Hugging Face 热度、引用数与 venue 信息。 |
| 结构化抽取 | 抽取研究问题、方法、贡献、局限、评测信号、风险与后续问题。 |
| 本地存储 | 按研究方向与 ISO 周写入 `data/` 下的 JSONL 记录。 |
| 静态 Dashboard | 基于本地数据生成可直接打开的静态审阅界面。 |
| Markdown 产物 | 生成周报、研究版图与审阅简报。 |
| 定时执行 | 支持通过 GitHub Actions 每日运行并提交数据更新。 |

## 快速开始

```bash
git clone https://github.com/TengJiao33/ArXiv_Daily_Digest.git
cd ArXiv_Daily_Digest
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

打开静态 Dashboard：

```text
index.html
```

根目录入口会跳转到：

```text
radar_dashboard/static/index.html
```

Dashboard 读取 `radar_dashboard/static/data.js`，可直接从本地文件系统打开。

## 采集流水线

运行完整采集流程：

```bash
python main.py
```

该命令可能访问 arXiv、Semantic Scholar、GitHub、Hugging Face、venue 查询接口以及豆包/火山 Ark。实际运行可能消耗 API 配额，取决于已配置的凭据和候选论文数量。

数据更新后，重新生成静态 Dashboard 快照：

```bash
python radar_dashboard/build_static.py
```

## 本地 Dashboard 服务

如需使用本地 API 模式：

```bash
python radar_dashboard/app.py
```

默认地址：

```text
http://127.0.0.1:7860
```

## 配置

需要外部集成时，在仓库根目录创建 `.env`：

```ini
DOUBAO_API_KEY=your_ark_api_key
DOUBAO_ENDPOINT_ID=your_endpoint_id
GITHUB_TOKEN=ghp_your_token
SEMANTIC_SCHOLAR_API_KEY=optional_s2_api_key
SERVERCHAN_SENDKEY=optional_serverchan_key
WXPUSHER_APP_TOKEN=optional_wxpusher_app_token
WXPUSHER_UIDS=optional_wxpusher_uids
```

GitHub Actions 使用同名 Secrets。定时工作流每日 UTC 03:00 运行。

## 研究方向

研究范围定义在：

```text
config/directions.yaml
```

每个方向可配置：

| 字段 | 用途 |
| --- | --- |
| `name` | Dashboard 与生成产物使用的显示名称。 |
| `description` | 提供给结构化抽取的方向描述。 |
| `arxiv_query` | arXiv 检索表达式。 |
| `keywords` | 用于补全和过滤逻辑的关键词。 |
| `relevance` | 相关性过滤所需的必备词与主题词。 |
| `max_papers` | 单方向候选数量上限。 |
| `seed_papers` | 用于直接纳入和引用扩展的 arXiv ID。 |

当前配置包含编辑可靠性、模型遗忘、Agent Harness、多 Agent 一致性、Agent 策略优化和事实性应用等方向。

## 权威锚点

已发表或经人工确认的高优先级论文可与每日候选队列分开维护：

```text
config/authority_anchors.yaml
```

这些记录会在 Dashboard 中展示，并在生成的简报中先于普通阅读队列列出。当前队列中识别到明确 venue 标签的论文也会在排序中获得更高优先级。

## 手动注入论文

当某篇论文需要进入完整补全流程，但不一定会被常规查询覆盖时，可使用手动注入：

```text
config/manual_papers.yaml
```

示例：

```yaml
manual_papers:
  agent-skills-harness:
    - arxiv_id: "2404.07972"
      reason: "Agent harness benchmark reference."
  factuality-rule-guided-apps:
    - "2412.08972"
```

手动注入会直接获取 arXiv 记录并跳过关键词相关性过滤。论文仍会经过代码检查、结构化抽取、Hugging Face 匹配、venue 标注和 JSONL 存储。历史去重会避免对已处理论文重复执行抽取。

## 审阅简报

基于本地记录生成 Markdown 简报：

```bash
python mentor_brief.py
```

默认输出：

```text
output/mentor_briefs/{ISO-week}.md
```

常用参数：

```bash
python mentor_brief.py --week 2026-W23 --top 3
python mentor_brief.py --stdout
```

## Venue 回填

Semantic Scholar venue 查询存在限流。当前 resolver 支持 `SEMANTIC_SCHOLAR_API_KEY` 或 `S2_API_KEY`，会将响应缓存在 `data/_cache/`，并在 429 时退避重试。

为已有记录回填 venue 标签：

```bash
python venue_backfill.py --week 2026-W23 --write
```

默认模式为 dry run，不写入文件：

```bash
python venue_backfill.py --week 2026-W23
```

## 项目结构

```text
ArXiv_Daily_Digest/
  index.html                    # 静态 Dashboard 入口
  config/                       # 研究方向、锚点与覆盖配置
  data/                         # JSONL 记录与生成的研究产物
  radar_dashboard/              # 静态 Dashboard 与可选本地 API 服务
  main.py                       # 采集流水线入口
  scraper_arxiv.py              # arXiv 采集
  relevance_filter.py           # 候选过滤
  citation_tracker.py           # Semantic Scholar 引用扩展
  code_hunter.py                # 代码仓库发现
  processor.py                  # 结构化抽取
  venue_resolver.py             # Venue 元数据解析
  digest_builder.py             # 周报生成
  landscape_builder.py          # 研究版图生成
  mentor_brief.py               # 本地审阅简报生成
  storage.py                    # JSONL 持久化与去重
  .github/workflows/daily.yml   # 定时采集工作流
```

## 数据产物

常见生成文件包括：

```text
data/{direction}/{ISO-week}/papers.jsonl
data/{direction}/{ISO-week}/weekly_digest.md
data/{direction}/{ISO-week}/landscape.md
radar_dashboard/static/data.js
output/mentor_briefs/{ISO-week}.md
```

## License

当前仓库未包含 license 文件。
