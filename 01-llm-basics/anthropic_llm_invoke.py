from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-sonnet-4-6")

response = llm.invoke("What is the capital of India?")

print(response.content)