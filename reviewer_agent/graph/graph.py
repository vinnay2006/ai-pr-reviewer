from langgraph.graph import StateGraph, END

from reviewer_agent.state.state import ReviewState
from reviewer_agent.nodes.diff_loader import diff_loader
from reviewer_agent.nodes.issue_detector import issue_detector
from reviewer_agent.nodes.comment_generator import comment_generator
from reviewer_agent.nodes.issue_validator import issue_validator
from reviewer_agent.nodes.diff_parser import diff_parser
builder = StateGraph(ReviewState)

builder.add_node("diff_loader", diff_loader)
builder.add_node("issue_detector", issue_detector)
builder.add_node("comment_generator", comment_generator)
builder.add_node(
    "issue_validator",
    issue_validator
)
builder.add_node(
    "diff_parser",
    diff_parser
)
builder.set_entry_point("diff_loader")

builder.add_edge(
    "diff_loader",
    "diff_parser"
)

builder.add_edge(
    "diff_parser",
    "issue_detector"
)
builder.add_edge(
    "issue_detector",
    "issue_validator"
)

builder.add_edge(
    "issue_validator",
    "comment_generator"
)
builder.add_edge("comment_generator", END)

graph = builder.compile()