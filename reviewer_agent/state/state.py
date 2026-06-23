from typing import TypedDict, List

class ReviewState(TypedDict):
    owner: str
    repo: str
    pr_number: int

    diff: str
    issues: list
    review_comments: list
    logs: list