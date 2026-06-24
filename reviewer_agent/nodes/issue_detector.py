import json
import re
from reviewer_agent.llm import llm

def issue_detector(state):

    diff = state["diff"]

    prompt = f"""
    You are a senior software engineer.

    Review the diff.

    Return ONLY JSON.

    Format:

    [
    {{
    "type": "",
    "severity": "",
    "file": "",
    "reason": ""
    }}
    ]

    Diff:
    {diff}
    """

    response = llm.invoke(prompt)
    content = response.content.strip()

    # remove markdown safely
    content = re.sub(r"```json|```", "", content).strip()

    try:
        issues = json.loads(content)

        # safety fallback
        if not isinstance(issues, list):
            issues = []

    except Exception:
        issues = [
            {
                "type": "unknown",
                "severity": "low",
                "reason": content
            }
        ]

    return {
        "issues": issues
    }