# Research Radar Dashboard

本地论文雷达仪表盘，读取仓库里的 `data/*/*/papers.jsonl`，不调用任何模型 API。

## Run

```bash
python radar_dashboard/app.py
```

默认地址：

```text
http://127.0.0.1:7860
```

## Features

- 本周论文数、带代码论文数、方向数量
- 近几周趋势
- 三个方向的主题分布
- 高频 limitations
- 带代码论文列表
- 论文浏览、方向筛选、周筛选、关键词搜索、theme 筛选
