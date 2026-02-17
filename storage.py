"""
数据存储模块
每次运行保存筛选结果和生成的报告，便于追溯和分析。
"""

import os
import json
from datetime import datetime


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def save_run_data(selected_papers, report, total_scanned=0):
    """
    保存单次运行的数据。
    存储路径: data/YYYY-MM-DD/
      - selected_papers.json  (AI 筛选后的论文数据)
      - report.md             (生成的推送报告)
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    run_dir = os.path.join(DATA_DIR, date_str)
    os.makedirs(run_dir, exist_ok=True)

    # 保存筛选后的论文数据
    save_data = {
        "date": date_str,
        "total_scanned": total_scanned,
        "total_selected": len(selected_papers),
        "papers": [],
    }

    for p in selected_papers:
        item = {
            "title": p.get("title", ""),
            "url": p.get("url", ""),
            "category": p.get("category", ""),
            "one_liner": p.get("one_liner", ""),
            "has_code": p.get("has_code", False),
            "repo_url": p.get("repo_url", ""),
            "repo_stars": p.get("repo_stars", 0),
        }
        # 深度摘要（如果有的话）
        if p.get("deep_summary"):
            item["deep_summary"] = p["deep_summary"]
        # 摘要只保留前 300 字预览
        if p.get("summary") and len(p["summary"]) > 300:
            item["summary_preview"] = p["summary"][:300] + "..."
        else:
            item["summary_preview"] = p.get("summary", "")

        save_data["papers"].append(item)

    raw_path = os.path.join(run_dir, "selected_papers.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2, default=str)
    print(f"[Storage] 筛选数据已保存: {raw_path}")

    # 保存报告
    report_path = os.path.join(run_dir, "report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"[Storage] 报告已保存: {report_path}")

    return run_dir
