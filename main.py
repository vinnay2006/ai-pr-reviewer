from reviewer_agent.graph.graph import graph

result = graph.invoke({
    "owner": "vinnay2006",
    "repo": "ai-pr-reviewer-test",
    "pr_number": 4,
    "diff": "",
    "commit_sha": "",
    "issues": [],
    "review_comments": [],
    "line_map": {},          # NEW
    "logs": []
})

print("\n=== Files Changed ===")
for file in result["files_changed"]:
    print(file)

print("\n=== Line Map ===")
for fname, lines in result.get("line_map", {}).items():
    print(f"{fname}: {lines}")

print("\n=== AI PR Review ===\n")
for issue, comment in zip(result["issues"], result["review_comments"]):
    print(f"Type: {issue['type']}")
    print(f"Severity: {issue['severity']}")
    print(f"File: {issue['file']}  Line: {issue['line']}")
    print(f"Reason: {issue['reason']}")
    print()
    print("Review Comment:")
    print(comment["body"])
    print("\n" + "-" * 50 + "\n")

print("\n=== FIXES ===\n")
for fix in result.get("fixes", []):
    print(fix)
    print("-" * 50)

print("\n=== PATCHES ===\n")
for patch in result.get("patches", []):
    print(patch)
    print("-" * 60)

print("\n=== Execution Logs ===\n")
for log in result["logs"]:
    print(log)