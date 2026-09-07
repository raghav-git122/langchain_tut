#FAISS, Pinecone, Chroma, Qdrant, Weaviate etc.
from langchain_classic.vectorstores import Chroma, FAISS, qdrant, pinecone
from langchain_openai import OpenAIEmbeddings

from langchain_classic.schema import Document

docs = [

]

vector_store = Chroma(
    embedding_function= OpenAIEmbeddings(),
    persist_directory='chroma_db',
    collection_name='sample'
)

vector_store.add_documents(docs)
#creates a sqlite3 DB with self generated ids

fetch = vector_store.get(include = ['embeddings', 'documents', 'metadatas'])

vector_store.similarity_search(
    query = 'write query to be compared here',
    k=2 #number of top results you want to fetch
)

#metadatas based filtering
vector_store.similarity_search_with_score(
    query=' ',
    filter={'metadata_object': 'object_value'}
)

updated_doc = Document(
    page_content=" ",
    metadata = { }
)
vector_store.update_document(document_id = '', document=updated_doc) #document id is the id of the document you wish to replace in the vector DB

#delete docs from vector DB
vector_store.delete(
    ids = ['']
)