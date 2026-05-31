# Knowledge Editing Radar Dashboard

本地研究雷达仪表盘，读取仓库里的 `data/*/*/papers.jsonl`，不调用任何模型 API。

Dashboard 只读取当前 `config/directions.yaml` 中配置的 active 方向；探索期旧数据会保留在磁盘上，但不会默认进入主视图。

## Static Mode

生成静态快照：

```bash
python radar_dashboard/build_static.py
```

然后直接打开：

```text
radar_dashboard/static/index.html
```

这个模式不需要启动端口，适合日常查看。采集数据变化后重新运行一次 `build_static.py` 即可刷新快照。

## Server Mode

```bash
python radar_dashboard/app.py
```

默认地址：

```text
http://127.0.0.1:7860
```

## Features

- 本周论文数、带代码论文数、方向数
- 近几周趋势
- 四条 knowledge editing / unlearning / reliability 子线概览
- 方法族分布
- A 会 venue 标签（ICLR / ICML / ACL / EMNLP / NeurIPS / AAAI 等）
- 失败模式聚合
- 评测信号聚合
- Idea hook 列表
- 带代码论文列表
- 论文浏览、方向筛选、周筛选、method family 筛选、关键词搜索
- 论文详情弹层：英文标题、中文标题、中文摘要、英文摘要、结构化提取字段、baseline、dataset、arXiv/PDF/code/venue 链接
