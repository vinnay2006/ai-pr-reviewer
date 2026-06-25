print("STARTING llm.py")

from dotenv import load_dotenv


load_dotenv()

import os
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)

print("LLM CREATED (gemini-mini)")

# class FakeResponse:
#     def __init__(self, content):
#         self.content = content


# class FakeLLM:
#     def invoke(self, prompt):

#         if "Return ONLY valid JSON" in prompt:
#             return FakeResponse("""
#             [
#                 {
#                     "type": "bug",
#                     "severity": "medium",
#                     "file": "DashboardShell.tsx",
#                     "reason": "Duplicate updateMilestoneAction call"
#                 }
#             ]
#             """)

#         return FakeResponse(
#             "Suggested fix: remove duplicate updateMilestoneAction call"
#         )


# llm = FakeLLM()



