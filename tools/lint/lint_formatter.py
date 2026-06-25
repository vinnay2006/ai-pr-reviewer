def format_lint_results(lint_issues):

    if not lint_issues:
        return "No lint issues found."

    lines = []

    for issue in lint_issues:
        lines.append(
            f"[{issue['severity'].upper()}] {issue['file']} "
            f"line {issue['line']} col {issue['column']} "
            f"— {issue['rule']}: {issue['message']}"
        )

    return "\n".join(lines)