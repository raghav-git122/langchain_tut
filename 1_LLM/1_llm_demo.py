import os
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

llm = OllamaLLM(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

prompt = "what is the capital of india?"

result = llm.invoke(prompt)

print(result)