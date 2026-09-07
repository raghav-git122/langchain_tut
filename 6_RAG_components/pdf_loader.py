#read pdf page by page which means each page appears as a component in the document list
#use pyPDF loader for text data not image/tabular data
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(__file_name.pdf__)

docs = loader.load()

print(docs)