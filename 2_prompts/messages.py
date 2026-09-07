import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

messages=[
    SystemMessage(content = 'You are a helpful assistant'),
    HumanMessage(content= 'Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages) 