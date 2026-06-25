
from typing import TypedDict

class ReviewState(TypedDict):

    owner: str
    repo: str
    pr_number: int
    commit_sha: str        # NEW — required by GitHub inline comment API

    diff: str
    files_changed: list

    lint_results: str
    test_results: str
    security_results: str
    patches: list
    issues: list           # each issue now includes "file" and "line"
    fixes: list

    review_comments: list  # each item now: {"path": ..., "line": ..., "body": ...}
    logs: list