def comment_generator(state):
    comments = []

    for issue in state["issues"]:
        comments.append(
            f"[{issue['severity'].upper()}] {issue['reason']}"
        )

    return {
        "review_comments": comments
    }