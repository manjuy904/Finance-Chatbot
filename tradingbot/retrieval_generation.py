from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from tradingbot.data_ingestion import ingestdata

def generation(vstore):
    # To retriev; I will convert my vector store into retrieval
    retriever = vstore.as_retriever(search_kwargs={"k" : 3}) # configures vector store to retrieve the top 3 most similar items to any given query vector (raised by user)
    
    # now I will define my Prompt
    FINANCE_BOT_TEMPLATE = """
    Your finance bot is an expert in finance related advice.
    Ensure your answers are relevant to the query context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    
    """
    
    # Now will create my Prompt template
    prompt = ChatPromptTemplate.from_template(FINANCE_BOT_TEMPLATE)
    
    # Define model
    llm = ChatOpenAI()
    
    # create chain. whenevr I will invoke my chain I will get final answer
    chain = (
        {"context": retriever, "question": RunnablePassthrough()} # Runnablepassthrough - for taking the query in the run time
        | prompt
        | llm
        | StrOutputParser() # StrOutputParse - for giving the final answer
    )
    
    return chain


if __name__ == '__main__':
    vstore = ingestdata("None")
    chain = generation(vstore)
    # I will invoke my chain here. here I will get answer from LLM
    print(chain.invoke("what is Market For Registrant’s Common Equity?"))
    