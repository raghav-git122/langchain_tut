import os
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
    temperature=1.1,
)

prompt = "what is the capital of india?"

result = model.invoke(prompt)

print(result.content)