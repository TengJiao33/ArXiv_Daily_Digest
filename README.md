# Knowledge Editing Direction Radar

> 前身：ArXiv Daily Digest / Research Radar
> 现在：围绕 **knowledge editing / unlearning / reliability** 的定向研究雷达。

2026-05-31 起，这个项目从“帮我寻找研究方向”的探索工具，转为“在确定研究空间内持续追踪问题、方法、评测和选题钩子”的研究基础设施。

---

## 这个项目是什么？

Knowledge Editing Direction Radar 每天自动追踪知识编辑、模型遗忘和编辑可靠性相关论文，并把论文摘要转换成适合研究决策的结构化信号。

它关心的不只是“今天有什么新论文”，而是：

- 这篇论文属于哪个 **method family**
- 它编辑或遗忘的对象是什么
- 它的评测信号是 locality、generality、specificity、portability、robustness，还是 retain-forget tradeoff
- 它暴露了什么 failure mode
- 它有没有代码、benchmark 或可复现工具
- 它能不能接出一个值得继续想的 idea hook

RA 工作是现实入口，但系统本身不把具体人名或组名写成显式规则；默认追踪的是学术方向、方法生态和可复现证据。

---

## 当前追踪方向

在 `config/directions.yaml` 中配置，当前四条 active 子线是：

| 方向 | 说明 | 代表种子 |
|------|------|----------|
| **知识编辑核心方法** | ROME、MEMIT、MEND、SERAC、KN 等参数/记忆层面的知识编辑方法与后续改进 | KN、MEND、ROME、SERAC、MEMIT |
| **模型遗忘与反知识编辑** | LLM unlearning、选择性遗忘、隐私/安全知识移除、保留-遗忘权衡 | TOFU |
| **编辑可靠性与评测** | locality、generality、specificity、portability、robustness、side effect、sequential editing | Editing LLMs survey、AlphaEdit |
| **编辑框架、工具与基准** | EasyEdit、EasyEdit2、benchmark、toolkit、方法集成与复现工具链 | EasyEdit、EasyEdit2、AlphaEdit |

第一版 seed anchors：

- KN: `2104.08696`
- MEND: `2110.11309`
- ROME: `2202.05262`
- SERAC: `2206.06520`
- MEMIT: `2210.07229`
- Editing LLMs survey: `2305.13172`
- EasyEdit: `2308.07269`
- Comprehensive KE study: `2401.01286`
- TOFU: `2401.06121`
- AlphaEdit: `2410.02355`
- EasyEdit2: `2504.15133`

---

## 核心流程

每天 GitHub Actions 自动运行：

1. **定向搜索**：按四条子线的 ArXiv 查询语句搜索最新论文。
2. **引用追踪**：通过 Semantic Scholar 追踪种子论文的被引者。
3. **相关性过滤**：按方向配置过滤泛领域噪声。
4. **去重**：跳过已存在论文，只对新论文调 API。
5. **代码检测**：检查是否有 GitHub 仓库和 stars。
6. **结构化提取**：豆包从摘要提取 `title_zh / abstract_zh / problem / method / method_family / edit_target / evaluation_signal / failure_mode / idea_hook / read_priority / direction_fit` 等字段。
7. **Venue 标注**：先读 `config/venue_overrides.yaml` 的人工确认标签，再用 Semantic Scholar 补全 ICLR / ICML / ACL / EMNLP / NeurIPS / AAAI 等 venue。
8. **存储**：追加写入 `data/{direction}/{ISO-week}/papers.jsonl`。
9. **周报与版图**：每周日自动生成 `weekly_digest.md` 和 `landscape.md`。

---

## 本地 Dashboard

默认使用静态入口，不需要启动端口：

```bash
python radar_dashboard/build_static.py
```

```text
radar_dashboard/static/index.html
```

需要实时 API 时，也可以启动 server mode：

```bash
python radar_dashboard/app.py
```

默认地址是 `http://127.0.0.1:7860`。

Dashboard 默认读取当前 `directions.yaml` 中的 active 方向，因此旧探索期数据不会占据主视图。它会展示：

- 本周论文、代码论文和方向数量
- 近几周趋势
- 方法族分布
- failure mode 聚合
- evaluation signal 聚合
- ICLR / ICML / ACL / EMNLP 等彩色 venue 标签
- idea hook 列表
- 带代码论文
- 可按方向、周、method family 和关键词筛选的论文卡片；点开详情后展示标题、中文标题、中文摘要、英文摘要、提取字段、数据集、baseline 和链接

---

## 数据与归档

旧目录仍保留在 `data/` 下，不删除、不迁移：

- `data/llm-truthfulness/`
- `data/representation-engineering/`
- `data/mechanistic-interpretability/`

这些是探索期 archive，记录从泛化找方向到定向研究空间的转变。新数据会按新的四条方向自动创建目录。

---

## 项目结构

```text
ArXiv_Daily_Digest/
├── config/
│   ├── directions.yaml          # 当前 active 研究方向
│   └── venue_overrides.yaml      # 人工确认的会议/期刊标签
├── data/                        # JSONL 数据、周报、研究版图
├── radar_dashboard/             # 本地研究视图
├── main.py                      # 主流程编排
├── scraper_arxiv.py             # ArXiv 定向搜索
├── citation_tracker.py          # Semantic Scholar 引用追踪
├── relevance_filter.py          # 方向相关性过滤
├── processor.py                 # 豆包结构化提取
├── doubao_client.py             # 豆包 API 客户端
├── storage.py                   # JSONL 存储与全局去重
├── digest_builder.py            # 周报生成
├── landscape_builder.py         # 方法版图生成
├── code_hunter.py               # GitHub 仓库检测
├── hf_daily.py                  # HuggingFace Daily Papers 热度补充
├── venue_resolver.py            # A 会 venue 标签识别与补全
├── notifier.py                  # Server 酱 / WXPusher 推送
└── .github/workflows/daily.yml  # 每日自动采集
```

---

## 快速开始

```bash
git clone https://github.com/TengJiao33/ArXiv_Daily_Digest.git
cd ArXiv_Daily_Digest
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

配置 `.env`：

```ini
DOUBAO_API_KEY=你的_ark_api_key
DOUBAO_ENDPOINT_ID=你的_endpoint_id
GITHUB_TOKEN=ghp_你的_token
SERVERCHAN_SENDKEY=你的_sendkey
```

运行采集：

```bash
python main.py
```

注意：`python main.py` 会访问外部 API 并消耗豆包额度；本地查看已有数据只需要启动 dashboard。

---

## 自动化

GitHub Actions 保持每日运行：北京时间 11:00。

仓库 Secrets 需要配置：

- `DOUBAO_API_KEY`
- `DOUBAO_ENDPOINT_ID`
- `GITHUB_TOKEN`
- 可选：`SERVERCHAN_SENDKEY`
- 可选：`WXPUSHER_APP_TOKEN`
- 可选：`WXPUSHER_UIDS`

---

## License

MIT License
