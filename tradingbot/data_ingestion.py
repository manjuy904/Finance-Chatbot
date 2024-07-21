
from langchain_astradb import AstraDBVectorStore
from langchain_openai import  AzureOpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from tradingbot.helper import load_file
import os

load_dotenv()

# Retrieve environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOIN")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

# Define embedding model. Embeddings Model is responsible for converting text documents into vectors.
embedding = OpenAIEmbeddings(api_key = OPENAI_API_KEY)

# Ingest the data and we will ingest this data inside vector database. here we will use Astra db vector database
def ingestdata(status):
    vstore =  AstraDBVectorStore(
    embedding=embedding,
    collection_name="financebot",
    api_endpoint = ASTRA_DB_API_ENDPOINT,
    token = ASTRA_DB_APPLICATION_TOKEN,
    namespace = ASTRA_DB_KEYSPACE
        )
    
    storage = status
    
    if storage == None:
        docs=load_file()
        inserted_ids = vstore.add_documents(docs)
    else:
        return vstore
    
    return vstore, inserted_ids


if __name__=='__main__':
    vstore,inserted_ids=ingestdata(None) # Calls the ingestdata function with None as the argument.Since the status parameter is None, the function will load documents, 
    # add them to the vector store, and return both the vector store (vstore) and the IDs of the inserted documents (inserted_ids)
    print(f"\nInserted {len(inserted_ids)}, documents.") # Prints the number of documents that were inserted into the vector store
    results = vstore.similarity_search("Can you tell me the low budget sound basshead.") # similarity_search method of the vstore object.The method searches for documents similar 
    # to the query "Can you tell me the low budget sound basshead."
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")