# import requests
# import os

# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# headers = {
#     "Authorization": f"token {GITHUB_TOKEN}",
#     "Accept": "application/vnd.github.v3.diff"
# }

# def get_pr_diff(owner, repo, pr_number):

#     url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"

#     response = requests.get(url, headers=headers)

#     # 🔥 IMPORTANT: directly return diff text
#     return response.text
import requests

def get_pr_diff(owner, repo, pr_number):

    url = f"https://github.com/{owner}/{repo}/pull/{pr_number}.diff"

    response = requests.get(url)

    return response.text