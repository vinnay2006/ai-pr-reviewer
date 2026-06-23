from reviewer_agent.llm import llm
import json

def issue_detector(state):

    diff = state["diff"]

    prompt = f"""
You are a senior software engineer reviewing a pull request.

Analyze the diff and return ONLY a JSON array.

Format:

[
  {{
    "type": "security",
    "severity": "high",
    "reason": "Password is logged."
  }}
]

Diff:
{diff}
"""

    response = llm.invoke(prompt)

    try:
        issues = json.loads(response.content)
    except:
        issues = [
            {
                "type": "unknown",
                "severity": "low",
                "reason": response.content
            }
        ]

    return {
        "issues": issues,
        "logs": [
        "Issue Detector completed"
    ]
    }