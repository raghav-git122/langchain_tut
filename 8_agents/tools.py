#built in tools exist
#from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

# search_tool = DuckDuckGoSearchRun()
# results = search_tool.invoke('top news in India')
# print(results)

# shell_tool = ShellTool()
# results = shell_tool.invoke('ls')
# out = shell_tool.invoke('whoami')
# print(results)
# print(out)

#find all inbuilt tools in langchian documentation

#__________________________________________________________________________________________________

#customtools
# from langchain_core.tools import tool

# @tool
# def multiply(a:int,b:int) -> int: #type hints are important
#     """multiply two numbers""" #doc strings are imoportant for llm to understand tool usecase
#     return a*b

# result = multiply.invoke({'a':3, 'b':10})

#__________________________________________________________________________________________________

# from langchain_core.tools import StructuredTool
# from pydantic import BaseModel, Field

# class MultiplyInput(BaseModel):
#     a: int = Field(required = True, description='The first number to add')
#     b: int = Field(required = True, description='The second number to add')

# multiply_tool = StructuredTool.from_function(
#     func = multiply,
#     mame = 'multiply',
#     description= 'Multiply two numbers',
#     args_schema=MultiplyInput
# )   

# result = multiply_tool.invoke({'a':3, 'b':10})
# print(result)

#__________________________________________________________________________________________________

from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required = True, description='The first number to add')
    b: int = Field(required = True, description='The second number to add')

class MultiplyTool(BaseTool):
    name: str = 'multiply'
    description: str = 'multiply two numbers'
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a : int, b : int) -> int:
        return a*b

multiply_tool = MultiplyTool()
result = multiply_tool.invoke({'a':2, 'b': 100})

print(result)