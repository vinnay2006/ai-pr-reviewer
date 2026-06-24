
from typing import TypedDict

class ReviewState(TypedDict):

    owner: str
    repo: str
    pr_number: int

    diff: str
    files_changed: list

    lint_results: str
    test_results: str
    security_results: str
    patches: list
    issues: list
    fixes: list

    review_comments: list
    logs: list