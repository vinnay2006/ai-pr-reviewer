from reviewer_agent.llm import llm

def comment_generator(state):

    comments = []

    for issue in state["issues"]:

        prompt = f"""
Write a professional GitHub review comment.

Issue Type:
{issue['type']}

Severity:
{issue['severity']}

Reason:
{issue['reason']}
"""

        response = llm.invoke(prompt)

        comments.append(response.content)

    return {
        "review_comments": comments
    }