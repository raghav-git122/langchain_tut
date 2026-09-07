from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

schema = [
    ResponseSchema(name='fact_1',  description = "Fact 1 about the topic"),
    ResponseSchema(name='fact_2',  description = "Fact 2 about the topic"),
    ResponseSchema(name='fact_2',  description = "Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'give 3 facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'topic':'black hole'})
result = model.invoke(prompt)
print(parser.parse(result.content))