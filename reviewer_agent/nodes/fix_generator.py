from reviewer_agent.llm import llm

def fix_generator(state):

    issues = state.get("issues", [])
    diff = state.get("diff", "")

    fixes = []

    for issue in issues:

        prompt = f"""
You are a senior software engineer.

Issue:
Type: {issue.get("type")}
Severity: {issue.get("severity")}
Reason: {issue.get("reason")}

Git Diff:
{diff}

Provide:
1. Root cause
2. Suggested fix
3. Correct code snippet

Keep response concise.
"""

        response = llm.invoke(prompt)

        fixes.append(response.content)

    return {
        "fixes": fixes
    }