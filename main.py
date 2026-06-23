from reviewer_agent.graph.graph import graph

result = graph.invoke({
    "owner": "vinnay2006",
    "repo": "AOR-tracker",
    "pr_number": 76,
    "diff": "",
    "issues": [],
    "review_comments": [],
    "logs": []
})

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

print("\n=== Execution Logs ===\n")

for log in result["logs"]:
    print(log)