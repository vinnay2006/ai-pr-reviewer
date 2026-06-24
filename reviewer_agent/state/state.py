from typing import TypedDict

class ReviewState(TypedDict):
    owner: str
    repo: str
    pr_number: int

    
    diff: str
    issues: list
    review_comments: list
    logs: list
    lint_results: str
    files_changed: list
    security_results: str
   