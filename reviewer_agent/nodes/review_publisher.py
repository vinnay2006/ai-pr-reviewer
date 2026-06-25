from github.post_review import post_review

def review_publisher(state):

    logs = state.get("logs", [])

    # Check human approval
    if not state.get("approved", True):
        print("Skipping GitHub post — not approved.")
        logs.append("Review not posted — failed human approval gate.")
        return {"logs": logs}

    owner = state["owner"]
    repo = state["repo"]
    pr_number = state["pr_number"]
    commit_sha = state["commit_sha"]
    review_comments = state.get("review_comments", [])

    status, response = post_review(
        owner,
        repo,
        pr_number,
        commit_sha,
        review_comments
    )

    logs.append(f"GitHub Status: {status}")
    logs.append(f"GitHub Response: {response[:300]}")

    return {
        "logs": logs
    }