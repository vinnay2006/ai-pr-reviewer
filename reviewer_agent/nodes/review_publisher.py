from github.review_publisher import post_review_comment

def review_publisher(state):

    owner = state["owner"]
    repo = state["repo"]
    pr_number = state["pr_number"]

    comments = state.get("review_comments", [])

    for comment in comments:
        post_review_comment(
            owner,
            repo,
            pr_number,
            comment
        )

    logs = state.get("logs", [])
    logs.append("Review comments published")

    return {
        "logs": logs
    }