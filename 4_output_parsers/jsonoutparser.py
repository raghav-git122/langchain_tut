from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

parser = JsonOutputParser()
#create a parser object and within the prompt itself define the format instructions of a json schema using partial variables

template = PromptTemplate(
    template = 'give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)
# print(parser.parse(result.content))

chain = template | model | parser
result = chain.invoke({})
print(result)