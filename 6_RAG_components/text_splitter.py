from langchain_text_splitters import CharacterTextSplitter

text = """
"""

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_text(text)

print(result)
#get different chunks as elements of a list