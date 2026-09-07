from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

class Person(BaseModel):
    name:str=Field(description='name of the person')
    age:int = Field(gt=18, description='age of the person')
    city:str = Field(description='name of the city the person belogs to')

parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = 'generate the name, age, city of a fictional {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'indian'})
# result = model.invoke(prompt)
# print(parser.parse(result.content))

chain = template | model | parser

result = chain.invoke({'place':'indian'})
print(result)