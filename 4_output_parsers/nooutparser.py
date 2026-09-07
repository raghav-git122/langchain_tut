from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

#prompt1 --> detailed report
template1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables=['topic']
)

#prompt2 --> summarize
template2 = PromptTemplate(
    template = 'write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})
result = model.invoke(prompt1)
prompt2 = template2.invoke({'text':result.content})
result1 = model.invoke(prompt2)
print(result1.content)