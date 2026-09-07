#ollama doesn't host cloud embedding models :( --> code won't run!
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_community.retrievers import WikipediaRetriever
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

load_dotenv()

# retreiver = WikipediaRetriever(top_k_results=2, lang = 'en')

# query = 'Pakistan shares its boundary with India'
# docs = retreiver.invoke(query)

# for i,doc in enumerate(docs):
#     print(f'\n---Result {i+1} ---')
#     print(f'Content: \n{doc.page_content}...')

documents = [
    Document(page_content='A brief armed conflict between India and Pakistan began after India launched missile strikes on Pakistan'),
    Document(page_content='commercial flights and normalcy reported from both countries'),
    Document(page_content='The Kashmir conflict, ongoing since 1947, has fuelled multiple wars and skirmishes'),
    Document(page_content='The name Pakistan was coined by Choudhry Rahmat Ali, a Pakistan Movement activist'),
]

embedding_model = OllamaEmbeddings(
    model="embeddinggemma",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

retreiver = vector_store.as_retriever(search_kwargs={'k':2})

query = 'indo-pak relations'

results = retreiver.invoke(query)

for i,doc in enumerate(results):
    print(f'\n---Result {i+1} ---')
    print(f'Content: \n{doc.page_content}...')