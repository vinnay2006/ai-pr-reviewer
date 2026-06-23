import json
import re
from reviewer_agent.llm import llm

def issue_detector(state):

    diff = state["diff"]

    prompt = f"""
You are a senior software engineer.

Return ONLY valid JSON array.
NO markdown, NO explanation.

Format:
[
  {{
    "type": "security",
    "severity": "high",
    "reason": "..."
  }}
]

Diff:
{diff}
"""

    response = llm.invoke(prompt)

    content = response.content

    # itll  Remove ```json ... ```
    content = re.sub(r"```json|```", "", content).strip()

    try:
        issues = json.loads(content)
    except:
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