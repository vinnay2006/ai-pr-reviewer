def fix_router(state):

    issues = state.get("issues", [])

    high_severity = [
        issue for issue in issues
        if issue.get("severity") == "high"
    ]

    if high_severity:

        print("\n=== HUMAN APPROVAL REQUIRED ===")
        print(f"{len(high_severity)} high severity issue(s) detected:\n")

        for i, issue in enumerate(high_severity, 1):
            print(f"{i}. [{issue['severity'].upper()}] {issue['file']} line {issue['line']}")
            print(f"   Type: {issue['type']}")
            print(f"   Reason: {issue['reason']}")
            print()

        print("Do you want to post this review to GitHub? (yes/no): ", end="")

        try:
            user_input = input().strip().lower()
        except Exception:
            user_input = "no"

        if user_input != "yes":
            print("Review cancelled by human. Nothing posted to GitHub.")
            return {
                "approved": False,
                "logs": state.get("logs", []) + ["Review cancelled by human approval gate."]
            }

        print("Approved. Posting review to GitHub...\n")
        return {
            "approved": True,
            "logs": state.get("logs", []) + ["Human approved high severity review."]
        }

    # No high severity — auto approve
    print("\n=== AUTO APPROVED (no high severity issues) ===\n")
    return {
        "approved": True,
        "logs": state.get("logs", []) + ["Auto approved — no high severity issues."]
    }