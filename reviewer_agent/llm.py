print("STARTING llm.py")

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

print("LLM CREATED (OpenAI GPT-4o-mini)")



