def issue_detector(state):
    diff = state["diff"]

    issues = []

    if "password" in diff:
        issues.append(
            {
                "type": "security",
                "severity": "high",
                "reason": "Sensitive password is being logged."
            }
        )

    return {
        "issues": issues
    }