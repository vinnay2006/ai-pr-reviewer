import requests
import os
from dotenv import load_dotenv
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("Token exists:", GITHUB_TOKEN is not None)

def post_review(owner, repo, pr_number, comments):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"

    body = {
        "body": "\n\n".join(comments),
        "event": "COMMENT"
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