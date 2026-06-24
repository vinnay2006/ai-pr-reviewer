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

You are given outputs from real tools:
- Lint tool
- Test runner
- Security scanner
- Git diff

Your job:
1. Identify REAL issues only (avoid duplicates / noise)
2. Prioritize by severity
3. Use tool outputs as truth, not guesses
4. Map issues to correct files

---

FILES CHANGED:
{files}

---

LINT RESULTS:
{lint_results}

---

TEST RESULTS:
{test_results}

---

SECURITY RESULTS:
{security_results}

---

GIT DIFF:
{diff}

---

Return ONLY valid JSON (no markdown):

[
  {{
    "type": "bug | security | style",
    "severity": "low | medium | high",
    "file": "",
    "reason": ""
  }}
]
"""

    response = llm.invoke(prompt)
    content = response.content.strip()

    # remove markdown wrappers if any
    content = re.sub(r"```json|```", "", content).strip()

    try:
        issues = json.loads(content)

        # ensure it's a list
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
                "reason": issue.get("reason", "No reason provided")
            })

        return {"issues": cleaned}

    except Exception as e:
        print(" JSON PARSE ERROR:", e)
        print("RAW OUTPUT:\n", content)

        return {"issues": []}


def normalize_severity(sev):
    sev = str(sev).lower()

    if sev not in ["low", "medium", "high"]:
        return "low"

    return sev