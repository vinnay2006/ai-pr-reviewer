import json
import re
from reviewer_agent.llm import llm


def issue_detector(state):

    lint_results = state.get("lint_results", "")
    test_results = state.get("test_results", "")
    security_results = state.get("security_results", "")
    files = state.get("files_changed", [])
    diff = state.get("diff", "")

    prompt = f"""
You are a senior software engineer doing a PR review.

FILES CHANGED:
{files}

LINT RESULTS:
{lint_results}

TEST RESULTS:
{test_results}

SECURITY RESULTS:
{security_results}

GIT DIFF:
{diff}

Return ONLY valid JSON array (no markdown, no explanation, no backticks):

[
  {{
    "type": "bug | security | style",
    "severity": "low | medium | high",
    "file": "<filename>",
    "line": <integer>,
    "reason": "<explanation>"
  }}
]
"""

    response = llm.invoke(prompt)
    content = response.content.strip()

    print("=== RAW ===", repr(content[:300]))

    # Strip ALL variations of code fences
    content = re.sub(r"(?i)```json", "", content)
    content = re.sub(r"```", "", content)
    content = content.strip()

    try:
        issues = json.loads(content)

        if not isinstance(issues, list):
            print("LLM did not return a list")
            return {"issues": []}

        cleaned = []

        for issue in issues:
            if not isinstance(issue, dict):
                continue

            cleaned.append({
                "type": issue.get("type", "unknown"),
                "severity": normalize_severity(issue.get("severity", "low")),
                "file": issue.get("file", "unknown"),
                "line": int(issue.get("line", 1)),
                "reason": issue.get("reason", "No reason provided")
            })

        return {"issues": cleaned}

    except Exception as e:
        print("JSON PARSE ERROR:", e)
        print("FULL CONTENT:", repr(content))
        return {"issues": []}


def normalize_severity(sev):
    sev = str(sev).lower()
    if sev not in ["low", "medium", "high"]:
        return "low"
    return sev