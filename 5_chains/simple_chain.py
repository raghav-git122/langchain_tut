from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

prompt = PromptTemplate(
    template = 'generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'badminton'})

print(result)

chain.get_graph().print_ascii()