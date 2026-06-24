from github.review_publisher import post_review

def review_publisher(state):

    owner = state["owner"]
    repo = state["repo"]
    pr_number = state["pr_number"]

    comments = state.get("review_comments", [])

    for comment in comments:
        post_review(
            owner,
            repo,
            pr_number,
            comment
        )

    logs = state.get("logs", [])
    status, response = post_review( state["owner"],
    state["repo"],
    state["pr_number"],
    state["review_comments"])

    logs.append(f"GitHub Status: {status}")
    logs.append(f"GitHub Response: {response[:300]}")

    return {
        "logs": logs
    }