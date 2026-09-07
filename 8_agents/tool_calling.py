from langchain_ollama import ChatOllama
import os
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

#toolcreate
@tool
def multiply(a:int, b: int)-> int:
    """given 2 numbers a and b, this tool returns their product"""
    return a*b

#toolbind
model_with_tools = model.bind_tools([multiply])

#toolcall
# result = model_with_tools.invoke('multiply 5 and 7').tool_calls[0]
# print(result)

#toolexecution
# tool_execution = multiply.invoke(result)
# print(tool_execution)

#entire pipeline
query = HumanMessage('can you multiply 89 with 38')
messages = [query]
result = model_with_tools.invoke(messages)
messages.append(result)
tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)
out = model_with_tools.invoke(messages)
print(out.content)