#directory loader runs with all document_loaders
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path = 'folder_path',
    glob = '*pdf',
    loader = PyPDFLoader
)

docs = loader.load()

#for large number of files in the directory use LazyLoader

docs = loader.lazy_load()