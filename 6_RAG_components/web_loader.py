from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader('https://docs.langchain.com/oss/python/integrations/document_loaders')

page = loader.load()

print(page[0],page_content)