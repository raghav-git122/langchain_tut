from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage, ToolMessage
import requests
from typing import Annotated

load_dotenv()

@tool
def get_conversion_factor(base_currency:str, target_currency:str)-> float:
    """this function fetches the currency conversion factor between base currency and target currency"""
    url = f'https://v6.exchangerate-api.com/v6/5f18fc126f24b2e7ce83c76d/pair/{base_currency}/{target_currency}'
    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_value:int, conversion_rate:Annotated[float, InjectedToolArg])-> float:
    """given a currency conversion rate, this function calculates the target currency value from a given base currency"""
    return base_currency_value*conversion_rate

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

model_with_tools = model.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage('What is the conversion factor between USD and INR, and based on that convert 10 usd to inr')]

ai_message = model_with_tools.invoke(messages)
messages.append(ai_message)

print("first tool_calls:", ai_message.tool_calls)

# execute whatever tool(s) the model asked for, feed results back
for tool_call in ai_message.tool_calls:
    if tool_call['name'] == 'get_conversion_factor':
        tool_result = get_conversion_factor.invoke(tool_call['args'])
        conversion_rate = tool_result['conversion_rate']
        messages.append(ToolMessage(content=str(tool_result), tool_call_id=tool_call['id']))
    elif tool_call['name'] == 'convert':
        # conversion_rate is an InjectedToolArg, so the model never supplies it -
        # we inject it ourselves before invoking the tool
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_result = convert.invoke(tool_call['args'])
        messages.append(ToolMessage(content=str(tool_result), tool_call_id=tool_call['id']))

# ask the model again now that it has the conversion factor - it should call convert this time
ai_message = model_with_tools.invoke(messages)
messages.append(ai_message)

print("second tool_calls:", ai_message.tool_calls)

for tool_call in ai_message.tool_calls:
    if tool_call['name'] == 'get_conversion_factor':
        tool_result = get_conversion_factor.invoke(tool_call['args'])
        conversion_rate = tool_result['conversion_rate']
        messages.append(ToolMessage(content=str(tool_result), tool_call_id=tool_call['id']))
    elif tool_call['name'] == 'convert':
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_result = convert.invoke(tool_call['args'])
        messages.append(ToolMessage(content=str(tool_result), tool_call_id=tool_call['id']))

# final natural-language answer
final_message = model_with_tools.invoke(messages)
print(final_message.content)