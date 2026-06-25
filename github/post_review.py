import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def post_review(owner, repo, pr_number, commit_sha, review_comments):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"

    # Build inline comments array for GitHub API
    inline_comments = []

    for comment in review_comments:
        if isinstance(comment, dict) and comment.get("path") and comment.get("line"):
            inline_comments.append({
                "path": comment["path"],
                "line": comment["line"],
                "body": comment["body"]
            })

    body = {
        "commit_id": commit_sha,
        "body": "AI PR Review — see inline comments below.",
        "event": "COMMENT",
        "comments": inline_comments
    }

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    return response.status_code, response.text