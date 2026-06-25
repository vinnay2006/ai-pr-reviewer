from reviewer_agent.llm import llm

def comment_generator(state):

    comments = []

    for issue in state["issues"]:

        prompt = f"""
Write a professional GitHub inline review comment.

Issue Type: {issue['type']}
Severity: {issue['severity']}
Reason: {issue['reason']}

Be concise. 2-4 sentences max. No headers. Plain text only.
"""

        try:
            response = llm.invoke(prompt)

            comments.append({
                "path": issue["file"],
                "line": issue["line"],
                "body": response.content.strip()
            })

        except Exception as e:
            print(f"LLM ERROR: {e}")

            comments.append({
                "path": issue.get("file", "unknown"),
                "line": issue.get("line", 1),
                "body": f"Issue detected: {issue['type']} — {issue.get('reason', '')}"
            })

    return {
        "review_comments": comments
    }