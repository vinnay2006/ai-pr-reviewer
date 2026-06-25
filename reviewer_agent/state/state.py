from typing import TypedDict

class ReviewState(TypedDict):

    owner: str
    repo: str
    pr_number: int
    commit_sha: str

    diff: str
    files_changed: list
    line_map: dict

    lint_results: str
    test_results: str
    security_results: str
    patches: list
    issues: list
    fixes: list

    review_comments: list
    approved: bool          # NEW
    logs: list