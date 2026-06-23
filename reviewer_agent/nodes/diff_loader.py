from github.github_client import get_pr_diff

def diff_loader(state):

    owner = state["owner"]
    repo = state["repo"]
    pr_number = state["pr_number"]

    diff = get_pr_diff(owner, repo, pr_number)
    print("DIFF OUTPUT:\n", diff[:500])
    return {
        **state,
        "diff": diff
    }