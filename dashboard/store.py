import json
import os
from datetime import datetime

STORE_PATH = os.path.join(os.path.dirname(__file__), "reviews.json")


def save_review(owner, repo, pr_number, issues, logs):

    reviews = _load()

    reviews.append({
        "id": len(reviews) + 1,
        "owner": owner,
        "repo": repo,
        "pr_number": pr_number,
        "pr_url": f"https://github.com/{owner}/{repo}/pull/{pr_number}",
        "issues": issues,
        "issue_count": len(issues),
        "high": len([i for i in issues if i.get("severity") == "high"]),
        "medium": len([i for i in issues if i.get("severity") == "medium"]),
        "low": len([i for i in issues if i.get("severity") == "low"]),
        "logs": logs,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    _save(reviews)


def get_all_reviews():
    return _load()


def get_stats():

    reviews = _load()

    if not reviews:
        return {
            "total_reviews": 0,
            "total_issues": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        }

    return {
        "total_reviews": len(reviews),
        "total_issues": sum(r["issue_count"] for r in reviews),
        "high": sum(r["high"] for r in reviews),
        "medium": sum(r["medium"] for r in reviews),
        "low": sum(r["low"] for r in reviews)
    }


def _load():
    if not os.path.exists(STORE_PATH):
        return []
    with open(STORE_PATH, "r") as f:
        return json.load(f)


def _save(reviews):
    with open(STORE_PATH, "w") as f:
        json.dump(reviews, f, indent=2)