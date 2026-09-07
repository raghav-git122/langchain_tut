# \n\n - para
# \n - line
# ' ' - word
# '' - character
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(chunks)

#markdown file splitter also available
#code splitter also available
splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 50
)

splitter.split_text(text)