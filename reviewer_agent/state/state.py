from typing import TypedDict, List

class ReviewState(TypedDict):
    diff: str
    issues: List[dict]
    review_comments: List[str]
    