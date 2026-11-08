import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

load_dotenv()

model = init_chat_model("openrouter:nemotron-3-ultra-550b-a55b",api_key = os.environ["OPENROUTER_API_KEY"],temperature = 0.7, max_tokens = 500)
response1 = model.invoke("What is Python?")
response2 = model.invoke("What is LangChain?")

print(response1.content)
print(response2.content)