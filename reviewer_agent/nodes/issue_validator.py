def issue_validator(state):

    issues = state.get("issues", [])

    seen = set()
    cleaned_issues = []

    for issue in issues:

        key = (
            issue.get("type", ""),
            issue.get("file", ""),
            issue.get("reason", "")[:50]
        )

        if key in seen:
            continue

        seen.add(key)

        severity = issue.get("severity", "low").lower()

        if severity not in ["low", "medium", "high"]:
            severity = "low"

        cleaned_issues.append({
            "type": issue.get("type", "unknown"),
            "severity": severity,
            "file": issue.get("file", "unknown"),
            "line": issue.get("line", 1),
            "reason": issue.get("reason", "No reason provided")
        })

    return {
        "issues": cleaned_issues
    }