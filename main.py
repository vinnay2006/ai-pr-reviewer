from reviewer_agent.graph.graph import graph

result = graph.invoke({
    "owner": "Get-North-Path",
    "repo": "AOR-tracker",
    "pr_number": 75,
    "diff": "",
    "issues": [],
    "review_comments": [],
    "logs": []
})
print("\n=== Files Changed ===")

for file in result["files_changed"]:
    print(file)

print("\n=== AI PR Review ===\n")

for issue, comment in zip(
    result["issues"],
    result["review_comments"]
):
    print(f"Type: {issue['type']}")
    print(f"Severity: {issue['severity']}")
    print(f"Reason: {issue['reason']}")
    print()

    print("Review Comment:")
    print(comment)

    print("\n" + "-" * 50 + "\n")
    print("\n=== FIXES ===\n")

for fix in result["fixes"]:
    print(fix)
    print("-" * 50)
    
print("\n=== PATCHES ===\n")

for patch in result.get("patches", []):
    print(patch)
    print("-" * 60)

print("\n=== Execution Logs ===\n")

for log in result["logs"]:
    print(log)