from reviewer_agent.graph.graph import graph

result = graph.invoke(
    {
        "diff": "",
        "issues": [],
        "review_comments": []
    }
)

print("\n=== AI PR Review ===\n")

for comment in result["review_comments"]:
    print(comment)