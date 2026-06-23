from reviewer_agent.llm import llm

def issue_detector(state):

    diff = state["diff"]

    prompt = f"""
You are a senior software engineer.

Analyze this PR diff.

Identify:
- Bugs
- Security issues
- Logic errors
- Missing edge cases

Return findings in plain English.

Diff:
{diff}
"""

    response = llm.invoke(prompt)

    return {
        "issues": [
            {
                "type": "analysis",
                "severity": "unknown",
                "reason": response.content
            }
        ]
    }