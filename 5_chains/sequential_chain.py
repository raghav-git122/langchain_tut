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

prompt1 = PromptTemplate(
    template = 'generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic':'badminton'})

print(result)

chain.get_graph().print_ascii()