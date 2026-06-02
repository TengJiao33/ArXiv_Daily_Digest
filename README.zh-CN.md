# ArXiv_Daily_Digest

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
![Dashboard](https://img.shields.io/badge/Dashboard-Static%20HTML%20%2B%20Local%20API-2f7d62)
![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![Scope](https://img.shields.io/badge/Scope-Agent%20Reliability%20Radar-3867a6)

[English](README.md)

ArXiv_Daily_Digest 是研究论文雷达和 dashboard 项目。当前核心界面是 **Agent Reliability Radar**，聚焦 LLM Agent、harness、可靠性、事实性、模型控制与安全干预。系统负责采集近期论文，补全代码、会议、引用和社区热度信号，抽取结构化研究字段，并通过本地 dashboard 和导师对齐 brief 形成日常阅读、选题判断入口。

## 核心功能

| 功能 | 定位 |
| --- | --- |
| 静态 Dashboard | 第一阅读入口。直接打开根目录 `index.html`，无需启动服务。 |
| 每日采集 | GitHub Actions 定时执行 ArXiv 搜索、引用扩展、相关性过滤、补全和 JSONL 存储。 |
| 方向雷达 | 当前 active 方向定义在 `config/directions.yaml`，保留 2 条旧线并新增 4 条吴小宝老师相关 agent / factuality 方向。 |
| 结构化抽取 | 从摘要中提取问题、方法、关键发现、方法族、控制机制、评测环境、可靠性风险、可行性和导师讨论问题。 |
| 导师 Brief | `mentor_brief.py` 把本地 JSONL 数据压缩成周期性导师对齐材料。 |

## Dashboard

直接打开根目录入口：

```text
index.html
```

该入口会跳转到：

```text
radar_dashboard/static/index.html
```

静态 dashboard 读取 `radar_dashboard/static/data.js`，可以直接从文件系统打开。采集数据更新后，重新生成静态快照：

```bash
python radar_dashboard/build_static.py
```

如果需要本地 API 模式：

```bash
python radar_dashboard/app.py
```

默认地址：

```text
http://127.0.0.1:7860
```

## 当前研究范围

| 方向 ID | 定位 |
| --- | --- |
| `editing-reliability-evaluation` | 旧线保留：编辑可靠性、steering 副作用、模型控制和机制干预。 |
| `model-unlearning` | 旧线保留并扩展：模型遗忘、后门防御、越狱防御和安全干预。 |
| `agent-skills-harness` | Agent skills、可执行 skill library、harness、tool-use control、workflow 约束和执行式评测。 |
| `multi-agent-consistency` | 多 Agent 协作、不一致、共识、辩论、judge/verifier 机制和行为一致性。 |
| `agent-policy-optimization` | 策略优化、在线蒸馏、teacher-student、reward learning、RLVR 和 test-time scaling。 |
| `factuality-rule-guided-apps` | 事实性、规则推理、幻觉检测、benchmark contamination 和应用场景评测。 |

## 导师 Brief

生成本地会前讨论材料，不访问外部 API：

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

## 快速开始

```bash
git clone https://github.com/TengJiao33/ArXiv_Daily_Digest.git
cd ArXiv_Daily_Digest
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

只有明确要调用外部 API 时才运行采集：

```bash
python main.py
```

`python main.py` 会访问 ArXiv、Semantic Scholar、GitHub、Hugging Face、venue 查询和豆包/火山 Ark，可能消耗 API 额度。打开 dashboard 和生成导师 brief 只读取本地文件。

## 配置

在仓库根目录创建 `.env`：

```ini
DOUBAO_API_KEY=your_ark_api_key
DOUBAO_ENDPOINT_ID=your_endpoint_id
GITHUB_TOKEN=ghp_your_token
SERVERCHAN_SENDKEY=optional_serverchan_key
WXPUSHER_APP_TOKEN=optional_wxpusher_app_token
WXPUSHER_UIDS=optional_wxpusher_uids
```

GitHub Actions 使用同名 Secrets。定时任务每天 UTC 03:00 运行，对应北京时间 11:00。

## 项目结构

```text
ArXiv_Daily_Digest/
  index.html                    # 点开即看的 dashboard 入口
  config/                       # active 方向与 venue override
  data/                         # JSONL 数据与生成的研究产物
  radar_dashboard/              # 静态 dashboard 和可选本地 API server
  main.py                       # 每日采集主流程
  processor.py                  # 结构化抽取
  mentor_brief.py               # 本地导师对齐 brief 生成器
  storage.py                    # JSONL 存储和方向级去重
  digest_builder.py             # 周报生成
  landscape_builder.py          # 研究版图生成
  .github/workflows/daily.yml   # 定时采集工作流
```

## License

当前仓库未包含 license 文件。
