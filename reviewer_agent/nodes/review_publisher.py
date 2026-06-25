from github.post_review import post_review

def review_publisher(state):

    owner = state["owner"]
    repo = state["repo"]
    pr_number = state["pr_number"]
    commit_sha = state["commit_sha"]             # NEW
    review_comments = state.get("review_comments", [])

    logs = state.get("logs", [])

    status, response = post_review(
        owner,
        repo,
        pr_number,
        commit_sha,                              # NEW
        review_comments
    )

    logs.append(f"GitHub Status: {status}")
    logs.append(f"GitHub Response: {response[:300]}")

    return {
        "logs": logs
    }