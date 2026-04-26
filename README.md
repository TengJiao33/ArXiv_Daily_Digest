# 🛰️ Research Radar — 研究方向定向雷达

> **前身**：ArXiv Daily Digest（论文早餐推送工具）  
> **现在**：一个帮你在写第一行代码之前，就知道该不该写的系统。

---

## 这个项目是什么？

这不是一个"论文推送工具"。

它的诞生源于一次失败的研究项目复盘：我们发现自己在没有地图的情况下，走进了一片已经被人翻遍的丛林。**我们缺的不是"读更多论文"的能力，而是一张持续更新的研究地图。**

Research Radar 做的事情是：

- 🎯 **定向追踪**多个研究方向，不是漫无目的地扫描
- 🧠 **豆包 AI 做苦力**：每天自动采集 + 结构化提取（便宜、稳定）
- 🤖 **Claude 做智囊**：你不定时带进来，对积累的数据做深度分析
- 📡 **双通道发现**：ArXiv 关键词搜索 + Semantic Scholar 引用追踪，弥补盲区

核心理念：**把"找到值得做的研究方向"这件事，从依赖导师经验和运气的黑箱，变成有工程支撑的、可复现的、AI 辅助的白箱流程。**

---

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                    Research Radar                            │
│                                                             │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │
│  │  📡 定向采集  │   │  🧠 结构提取  │   │  📊 数据积累  │    │
│  │              │   │              │   │              │    │
│  │ ArXiv 搜索   │──→│ 豆包 AI      │──→│ JSONL 存储   │    │
│  │ 引用追踪     │   │ problem      │   │ 按方向分类   │    │
│  │ 代码检测     │   │ method       │   │ 按 ISO 周    │    │
│  │              │   │ limitations  │   │ 自动去重     │    │
│  └──────────────┘   └──────────────┘   └──────────────┘    │
│           │                                    │            │
│     每天自动跑                          你带 Claude 来看     │
│    (GitHub Actions)                    (不定时深度分析)       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📡 当前追踪的研究方向

在 `config/directions.yaml` 中配置，随时可增删：

| 方向 | 说明 | 数据源 |
|------|------|--------|
| **LLM 真值性与事实性** | Know-Say Gap、幻觉机制、真值干预 | ArXiv + 3 篇种子论文引用网络 |
| **表示工程与激活引导** | Steering Vector、RepE、激活干预 | ArXiv + 1 篇种子论文引用网络 |
| **机械可解释性** | Circuit Analysis、SAE、Logit Lens | ArXiv |

---

## 🔧 核心流程

每天 GitHub Actions 自动运行：

1. **定向搜索**：按方向配置的 ArXiv 查询语句搜索最新论文
2. **引用追踪**：通过 Semantic Scholar 追踪种子论文的被引者（发现关键词搜不到的论文）
3. **去重**：跳过已存在的论文，只对新论文调 API（节省费用）
4. **代码检测**：检查是否有 GitHub 仓库、Stars 数
5. **结构化提取**：豆包 AI 从摘要中提取 `problem / method / contribution / limitations / baselines / datasets`
6. **存储**：追加写入 JSONL 文件，按 `data/{方向}/{ISO周}/papers.jsonl` 组织
7. **周报**：每周日自动生成周报（论文计数、高频 baseline、limitations 聚合）

---

## 📂 项目结构

```
ArXiv_Daily_Digest/
├── config/
│   └── directions.yaml        # 研究方向配置（查询词、种子论文、关键词）
├── data/
│   ├── llm-truthfulness/
│   │   └── 2026-W17/
│   │       ├── papers.jsonl    # 结构化论文数据
│   │       └── weekly_digest.md
│   ├── representation-engineering/
│   └── mechanistic-interpretability/
├── main.py                    # 主流程编排
├── scraper_arxiv.py           # ArXiv 定向搜索
├── citation_tracker.py        # Semantic Scholar 引用追踪
├── processor.py               # 豆包结构化提取
├── doubao_client.py           # 豆包 API 客户端
├── storage.py                 # JSONL 存储 + 去重
├── digest_builder.py          # 周报生成
├── code_hunter.py             # GitHub 代码仓库检测
├── notifier.py                # 推送（Server酱 / WXPusher）
└── .github/workflows/daily.yml
```

---

## 🚀 快速开始

### 1. 克隆 & 安装

```bash
git clone https://github.com/TengJiao33/ArXiv_Daily_Digest.git
cd ArXiv_Daily_Digest
python -m venv .venv && .venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. 配置 `.env`

```ini
# 豆包 AI (必填)
DOUBAO_API_KEY=你的_ark_api_key
DOUBAO_ENDPOINT_ID=你的_endpoint_id

# GitHub Token (可选，提高 API 限额)
GITHUB_TOKEN=ghp_你的_token

# 推送渠道 (可选)
SERVERCHAN_SENDKEY=你的_sendkey
```

### 3. 运行

```bash
python main.py
```

### 4. 自动化（GitHub Actions）

项目内置 GitHub Actions，每天北京时间 11:00 自动运行。

在仓库 **Settings → Secrets** 中配置 `DOUBAO_API_KEY`、`DOUBAO_ENDPOINT_ID`、`GH_PAT` 即可。

---

## 💡 两层设计哲学

| 层 | 执行者 | 频率 | 做什么 |
|----|--------|------|--------|
| **自动采集层** | 豆包（便宜） | 每天 | 搜论文、提取结构化信息、存 JSONL |
| **深度分析层** | Claude（强力） | 你来了就做 | 读积累的数据、发现趋势、找研究空白 |

**豆包是蚂蚁**：每天勤勤恳恳搬运数据，不需要你在场。  
**Claude 是参谋**：你带着它走进堆满数据的房间，它帮你看出规律。

---

## 📜 项目演化史

- **v0**（2026-02）：ArXiv Daily Digest — 每天推送 AI 论文到手机的"论文早餐"
- **v1**（2026-04-25）：Research Radar — 从消费型推送进化为生产型研究方向发现系统
- **v1.1**（2026-04-25）：引用追踪 + 去重优化

---

## 📄 License

MIT License
