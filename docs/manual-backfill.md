# 人工补录论文与 A 会标注

当重要论文没有被日常 arXiv 查询收录时，优先使用人工补录路径，而不是在本地直接运行完整采集流程。

## 适用场景

- ICLR、ICML、NeurIPS、ACL、EMNLP、AAAI、IJCAI 等 A 会论文已经接收，但发布时间早于当前 daily crawl 的 recent window。
- 论文题目或摘要命中了研究方向，但没有进入 `data/`。
- 论文已进入 `data/`，但 venue 仍为空或被识别成 `arXiv`。

## 推荐流程

1. 在 `config/manual_papers.yaml` 中，把论文加入最贴近的方向。
2. 在 `config/venue_overrides.yaml` 中，补稳定的 venue 标注。
3. 提交并推送配置变更。
4. 让下一次 GitHub Actions daily workflow 运行，或在 GitHub Actions 页面手动触发 `workflow_dispatch`。
5. workflow 使用 repository secrets 完成 Doubao 结构化抽取、外部元数据补全、JSONL 写入和 Dashboard 生成。
6. 运行结束后，从远程拉取 bot 提交的 `data/` 与 `radar_dashboard/static/data.js` 更新。

## 为什么不在本地跑完整流程

完整 `python main.py` 会调用 arXiv、Semantic Scholar、GitHub、Hugging Face、OpenReview、Doubao/Volcengine Ark，并可能触发通知推送。如果 Doubao、Semantic Scholar、通知服务等密钥只配置在 GitHub Actions secrets，本地运行会失败或得到不完整结果。

因此，本地只负责维护人工补录配置；真正的 enrichment 交给下一次 GitHub Actions 运行。

## OpenReview 与 Semantic Scholar

OpenReview 的公开页面和单篇公开 metadata 通常不需要单独 API key，但批量搜索很容易遇到 429 限流。Semantic Scholar 支持 `SEMANTIC_SCHOLAR_API_KEY` 或 `S2_API_KEY`，项目在 GitHub Actions 中使用 `SEMANTIC_SCHOLAR_API_KEY`。

对于已人工确认的 accepted paper，不要依赖 OpenReview 或 Semantic Scholar 每次都能即时查到 venue；直接在 `config/venue_overrides.yaml` 里写入 venue override。

## A 会识别

A 会白名单与 venue 归一化逻辑集中在 `venue_catalog.py`。Dashboard、mentor brief 和 venue resolver 应使用同一套规则，避免某些会议在一个页面被识别为 A 会、另一个页面却漏标。

新增会议或别名时，优先更新 `venue_catalog.py`，再补必要的 `config/venue_overrides.yaml`。
