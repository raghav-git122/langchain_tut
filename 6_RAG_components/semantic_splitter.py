from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1 #cuts at 1SD difference between chunks
)

sample = """
"""

print(splitter.split_text(sample))