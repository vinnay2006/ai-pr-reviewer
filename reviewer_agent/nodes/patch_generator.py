from reviewer_agent.llm import llm

def patch_generator(state):

    issues = state.get("issues", [])
    diff = state.get("diff", "")

    patches = []

    for issue in issues:

        prompt = f"""
You are a senior software engineer.

Issue:
Type: {issue.get("type")}
Severity: {issue.get("severity")}
Reason: {issue.get("reason")}

Git Diff:
{diff}

Generate ONLY a corrected code patch.

Return code only.
"""

        response = llm.invoke(prompt)

        patches.append(response.content)

    return {
        "patches": patches
    }