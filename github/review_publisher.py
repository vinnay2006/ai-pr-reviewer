import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def post_review_comment(owner, repo, pr_number, body):

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/issues/{pr_number}/comments"
    )

    response = requests.post(
        url,
        headers=headers,
        json={"body": body}
    )

    return response.status_code