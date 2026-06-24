# print("STARTING llm.py")

# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI

# load_dotenv()

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )

# print("LLM CREATED (OpenAI GPT-4o-mini)")

class FakeResponse:
    def __init__(self, content):
        self.content = content


class FakeLLM:
    def invoke(self, prompt):

        if "Return ONLY valid JSON" in prompt:
            return FakeResponse("""
            [
                {
                    "type": "bug",
                    "severity": "medium",
                    "file": "DashboardShell.tsx",
                    "reason": "Duplicate updateMilestoneAction call"
                }
            ]
            """)

        return FakeResponse(
            "Suggested fix: remove duplicate updateMilestoneAction call"
        )


llm = FakeLLM()



