
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def load_file():
    loader = PyPDFLoader("D:\\Industry prep\\Gen AI\\End to End Gen AI\\Finance-Chatbot\\data\\finance_data.pdf")
    pages = loader.load()

    # we have page content separetely. Now instead of taking pages separetely, I will store everything in one variable.
    # I will take empty variable
    # I will collect the content of the all pages
    raw_text = ''
    for i, doc in enumerate(pages): # enumerate means it will give indexes as well
        text = doc.page_content
        if text:
            raw_text += text
            
    text_splitter = RecursiveCharacterTextSplitter(   # this will give me chunks
        chunk_size = 500,   
        chunk_overlap = 100    
    )

    # text_splitter will split the data
    docs = text_splitter.split_text(raw_text)
    
    return(docs)