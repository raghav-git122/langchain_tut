from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

parser = StrOutputParser()

#defining the pydantic schema
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='return the sentiment of the feedback - either positive or negative')

parser2 = PydanticOutputParser(pydantic_object=Feedback) #parser verifies that the output is in infact of the given format

prompt1 = PromptTemplate(
    template = 'classify the sentiment of the following feedback text into positive or negative. \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='write an approprite response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='write an approprite response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback' : "the product is good!"})
print(result)
chain.get_graph().print_ascii()