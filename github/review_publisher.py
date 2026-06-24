from github.post_review import post_review


def review_publisher(state):

    status, response = post_review(
        state["owner"],
        state["repo"],
        state["pr_number"],
        state["review_comments"]
    )

    logs = state.get("logs", [])

    logs.append(
        f"GitHub review posted: {status}"
    )

    return {
        "logs": logs
    }