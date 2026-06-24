from langgraph.graph import StateGraph, END

from reviewer_agent.state.state import ReviewState

from reviewer_agent.nodes.diff_loader import diff_loader
from reviewer_agent.nodes.diff_parser import diff_parser
from reviewer_agent.nodes.lint_runner import lint_runner
from reviewer_agent.nodes.test_runner import test_runner
from reviewer_agent.nodes.security_runner import security_runner
from reviewer_agent.nodes.issue_detector import issue_detector
from reviewer_agent.nodes.issue_validator import issue_validator
from reviewer_agent.nodes.comment_generator import comment_generator
from reviewer_agent.nodes.fix_generator import fix_generator
from reviewer_agent.nodes.patch_generator import patch_generator
from reviewer_agent.nodes.review_publisher import review_publisher
builder = StateGraph(ReviewState)

# Nodes
builder.add_node("diff_loader", diff_loader)
builder.add_node("diff_parser", diff_parser)
builder.add_node("lint_runner", lint_runner)
builder.add_node("test_runner", test_runner)
builder.add_node("security_runner", security_runner)
builder.add_node("issue_detector", issue_detector)
builder.add_node("issue_validator", issue_validator)
builder.add_node("comment_generator", comment_generator)
builder.add_node(
    "fix_generator",
    fix_generator
)
builder.add_node(
    "patch_generator",
    patch_generator
)
builder.add_node(
    "review_publisher",
    review_publisher
)

# Entry
builder.set_entry_point("diff_loader")

# Flow
builder.add_edge("diff_loader", "diff_parser")
builder.add_edge("diff_parser", "lint_runner")
builder.add_edge("lint_runner", "test_runner")
builder.add_edge("test_runner", "security_runner")
builder.add_edge("security_runner", "issue_detector")
builder.add_edge("issue_detector", "issue_validator")
builder.add_edge(
    "issue_validator",
    "fix_generator"
)

builder.add_edge(
    "fix_generator",
    "patch_generator"
)

builder.add_edge(
    "patch_generator",
    "comment_generator"
)
builder.add_edge(
    "comment_generator",
    "review_publisher"
)

builder.add_edge(
    "review_publisher",
    END
)

graph = builder.compile()