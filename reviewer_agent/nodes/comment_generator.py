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

        try:
            response = llm.invoke(prompt)
            comments.append(response.content)

        except Exception as e:
            print(f"LLM ERROR: {e}")

            comments.append(
                f"Failed to generate comment for issue '{issue['type']}'. Error: {str(e)}"
            )

    return {
        "review_comments": comments
    }