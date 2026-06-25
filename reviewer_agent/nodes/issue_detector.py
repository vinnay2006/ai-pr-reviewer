import json
import re
from reviewer_agent.llm import llm


def issue_detector(state):

    lint_results = state.get("lint_results", "")
    test_results = state.get("test_results", "")
    security_results = state.get("security_results", "")
    files = state.get("files_changed", [])
    diff = state.get("diff", "")
    line_map = state.get("line_map", {})

    # Format line map for prompt
    line_map_str = ""
    for fname, lines in line_map.items():
        line_map_str += f"{fname}: lines {lines}\n"

    prompt = f"""
You are a senior software engineer doing a PR review.

FILES CHANGED:
{files}

VALID LINE NUMBERS PER FILE (only pick from these):
{line_map_str}

LINT RESULTS:
{lint_results}

TEST RESULTS:
{test_results}

SECURITY RESULTS:
{security_results}

GIT DIFF:
{diff}

Return ONLY valid JSON array (no markdown, no backticks):

[
  {{
    "type": "bug | security | style",
    "severity": "low | medium | high",
    "file": "<filename>",
    "line": <integer, must be from the valid line numbers above>,
    "reason": "<explanation>"
  }}
]
"""

    response = llm.invoke(prompt)
    content = response.content.strip()

    print("=== RAW ===", repr(content[:300]))

    content = re.sub(r"(?i)```json", "", content)
    content = re.sub(r"```", "", content).strip()

    try:
        issues = json.loads(content)

        if not isinstance(issues, list):
            print("LLM did not return a list")
            return {"issues": []}

        cleaned = []

        for issue in issues:
            if not isinstance(issue, dict):
                continue

            fname = issue.get("file", "unknown")
            raw_line = int(issue.get("line", 1))

            # Clamp to nearest valid line number
            valid_lines = line_map.get(fname, [])
            if valid_lines:
                line = min(valid_lines, key=lambda x: abs(x - raw_line))
            else:
                line = raw_line

            cleaned.append({
                "type": issue.get("type", "unknown"),
                "severity": normalize_severity(issue.get("severity", "low")),
                "file": fname,
                "line": line,
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