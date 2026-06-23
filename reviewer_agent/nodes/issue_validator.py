from reviewer_agent.llm import llm

def issue_validator(state):

    validated = []

    for issue in state["issues"]:

        prompt = f"""
You are a senior software engineer.

Issue:
{issue}

Determine whether this is a real issue.

Return only:
VALID
or
INVALID
"""

        response = llm.invoke(prompt)

        if "VALID" in response.content.upper():
            validated.append(issue)

    return {
        "issues": validated,
        "logs": [
        "Issue Validator completed"
    ]
    }