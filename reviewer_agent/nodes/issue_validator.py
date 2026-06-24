def issue_validator(state):

    issues = state.get("issues", [])

    seen = set()
    cleaned_issues = []

    for issue in issues:

        # create a unique key for deduplication
        key = (
            issue.get("type", ""),
            issue.get("file", ""),
            issue.get("reason", "")[:50]
        )

        # skip duplicates
        if key in seen:
            continue

        seen.add(key)

        # normalize severity
        severity = issue.get("severity", "low").lower()

        if severity not in ["low", "medium", "high"]:
            severity = "low"

        cleaned_issues.append({
            "type": issue.get("type", "unknown"),
            "severity": severity,
            "file": issue.get("file", "unknown"),
            "reason": issue.get("reason", "No reason provided")
        })

    return {
        "issues": cleaned_issues
    }