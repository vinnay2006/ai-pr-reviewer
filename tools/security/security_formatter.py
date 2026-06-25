def format_security_results(security_issues):

    if not security_issues:
        return "No security issues found."

    if isinstance(security_issues, str):
        return security_issues

    lines = []

    for issue in security_issues:
        lines.append(
            f"[{issue['severity'].upper()}] {issue['file']} "
            f"line {issue['line']} "
            f"— {issue['rule']}: {issue['message']} "
            f"(confidence: {issue['confidence']})"
        )

    return "\n".join(lines)