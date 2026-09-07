import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

#chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human','{query}')
]) 

chat_history=[]
#load chat history
with open('2_prompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

#create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'where the fuck is my refund'})

#get AI response
result = model.invoke(prompt)

print(result.content)