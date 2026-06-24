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