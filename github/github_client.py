import requests

def get_pr_diff(owner, repo, pr_number):

    url = f"https://github.com/{owner}/{repo}/pull/{pr_number}.diff"

    print("Fetching:", url)

    response = requests.get(url)

    if response.status_code == 404:
        raise Exception(
            f"PR not found. Check owner/repo/PR number:\n{url}"
        )

    if response.status_code != 200:
        raise Exception(
            f"Failed: {response.status_code}\n{response.text}"
        )

    return response.text


def get_pr_head_sha(owner, repo, pr_number):       # NEW

    import os
    from dotenv import load_dotenv
    load_dotenv()

    token = os.getenv("GITHUB_TOKEN")

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to get PR SHA: {response.status_code}")

    return response.json()["head"]["sha"]