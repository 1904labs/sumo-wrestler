from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from time import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f",
    "--file_path",
    type=str,
    help="Path to the PDF file to summarize",
    required=True,
)
parser.add_argument(
    "-c",
    "--chain_type",
    type=str,
    help='Open ai summary chain_type: "stuff", "map_reduce" or "refine"',
    default="map_reduce",
)

args = parser.parse_args()


def summarize(pdf_path, chain_type):
    # Load the PDF
    print(f"Loading PDF from path: {pdf_path}")
    loader = PyPDFLoader(file_path=pdf_path)

    # Split the PDF into chunks of text
    text_splitter = CharacterTextSplitter(
        chunk_size=750, chunk_overlap=100, separator="/n"
    )
    document = loader.load()
    docs = text_splitter.split_documents(documents=document)

    # Summarize throught openai
    llm = OpenAI(temperature=0)
    chain = load_summarize_chain(llm, chain_type=chain_type)
    openai_response = chain.run(docs)

    return openai_response


if __name__ == "__main__":
    chain_type = "map_reduce"
    pdf_path = "/Users/jocelynmatsuo/devdir/lab/vectorsource-in-memory/2210.03629.pdf"

    start = (
        time()
    )  # timing the method, because certain chain_types take a super long time

    print(summarize(pdf_path=args.file_path, chain_type=args.chain_type))

    print(f"Time to summarize using chain_type = {chain_type}: {time() - start}")
