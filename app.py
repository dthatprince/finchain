import os
import re
from langchain.chat_models import ChatOpenAI
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)
import chromadb


# Set API Key
os.environ["OPENAI_API_KEY"] = " "

# LLM & Embeddings
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
embedding_function = OpenAIEmbeddings()

# Load PDF and split into pages
loader = PyPDFLoader("data/annualreport.pdf")
pages = loader.load_and_split()

# Load into Chroma vector database (in-memory or persistent as needed)
store = Chroma.from_documents(
    pages, embedding_function, collection_name="annualreport", persist_directory="./chroma_db"
)

# Optional: Clear Chroma system cache (if needed)
chromadb.api.client.SharedSystemClient.clear_system_cache()


# Vectorstore info
vectorstore_info = VectorStoreInfo(
    name="annual_report",
    description="A banking annual report as a PDF document",
    vectorstore=store
)

# Create toolkit
toolkit = VectorStoreToolkit(
    vectorstore_info=vectorstore_info,
    llm=llm
)

# Agent to query the vectorstore
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# Text Cleaning Helper Function
def clean_extracted_text(text):
    # Fixes spaced-out characters like "n e t p r o f i t"
    cleaned_text = re.sub(r'(?<!\s)([a-zA-Z])\s(?=[a-zA-Z])', r'\1', text)
    # Normalize spaces and remove extra line breaks
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

# Streamlit UI
st.title('Q&A Investment Advisor App')

# User input box
prompt = st.text_input("Enter your question here")

# Display sample questions below the input box
st.markdown(
    """
    **Example Questions:**  
    - What was the company's net profit?  
    - What sustainability initiatives did the bank implement?  
    - Provide a summary of the bank's financial performance.
    """
)

if prompt:
    # Use agent_executor for the query
    response = agent_executor.run(prompt)

    # Clean up the response text if it appears messy
    cleaned_response = clean_extracted_text(response)

    # Optionally ask GPT to format it for readability (Clarifying the response)
    clarification_prompt = f"""
    Please reformat the following financial data summary to be clear, concise, and easy to read:
    {cleaned_response}
    """
    formatted_response = llm.predict(clarification_prompt)

    # Display the cleaned and formatted response
    st.write(formatted_response)

    # Optional: Show document similarity search results
    with st.expander('Document Similarity Search'):
        search = store.similarity_search_with_score(prompt)
        st.write(search[0][0].page_content)
