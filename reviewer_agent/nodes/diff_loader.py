from github.github_client import get_pr_diff, get_pr_head_sha

def diff_loader(state):

    owner = state["owner"]
    repo = state["repo"]
    pr_number = state["pr_number"]

    diff = get_pr_diff(owner, repo, pr_number)
    commit_sha = get_pr_head_sha(owner, repo, pr_number)   # NEW

    print("DIFF OUTPUT:\n", diff[:500])
    print("COMMIT SHA:", commit_sha)

    return {
        **state,
        "diff": diff,
        "commit_sha": commit_sha    # NEW
    }