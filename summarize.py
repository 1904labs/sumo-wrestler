from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain import OpenAI


def summarize(pdf_path):
    # Load the PDF
    print(f"Loading PDF from path: {pdf_path}")
    loader = PyPDFLoader(file_path = pdf_path)

    prompt = """Give me a 2 sentence summary of the following text: \n"""

    # Split the PDF into chunks of text
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100, separator="/n")
    document = loader.load()
    docs = text_splitter.split_documents(documents = document)

    # Create a vectorstore from the documents to use for retrieval
    embeddings = OpenAIEmbeddings()
    vectorstore =  FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index_pdfs")
    new_vectorstore = FAISS.load_local("faiss_index_pdfs", embeddings=embeddings)
    
    # Query OpenAI to summarize the docuemtns
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever = new_vectorstore.as_retriever())

    openai_response = qa.run(prompt)

    return openai_response


if __name__ == "__main__":
    pdf_path = "/Users/jocelynmatsuo/devdir/lab/vectorsource-in-memory/2210.03629.pdf"
    print(summarize(pdf_path=pdf_path))