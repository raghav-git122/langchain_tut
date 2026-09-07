from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
text = """
"""

loader = PyPDFLoader('file_location/file_name.pdf')

doc = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_documents(doc)

print(result)
#get different chunks as elements of a list