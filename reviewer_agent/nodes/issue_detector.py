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
    {
        "type": "bug | security | style",
        "severity": "low | medium | high",
        "file": "",
        "reason": ""
    }
    ]
    """

    response = llm.invoke(prompt)
    content = response.content.strip()

    # remove markdown safely
    content = re.sub(r"```json|```", "", content).strip()

    try:
        issues = json.loads(content)

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