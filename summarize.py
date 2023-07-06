from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from time import time
import argparse

# Parse arguments (-h help is automatically generated)
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

parser.add_argument(
    "-s",
    "--chunk_size",
    type=int,
    help="Size of the chunks to split the PDF into",
    default=750,
)

parser.add_argument(
    "-o",
    "--chunk_overlap",
    help="Amount of overlap between split chunks of PDF",
    default=100,
)

args = parser.parse_args()


def summarize(pdf_path, chain_type, chunk_size, chunk_overlap) -> str:
    """Summarize a pdf using openai
    Takes a
    Required File path to a pdf,
    Optional chain_type (strategy to call openai to generate summary)
    Optional chunk_size (size of the chunks to split the pdf into)
    Optional chunk_overlap (amount of overlap between chunks)
    Returns a summary of the pdf from openai
    """

    # Load the PDF from file_path
    print(f"Loading PDF from path: {pdf_path}")
    loader = PyPDFLoader(file_path=pdf_path)

    # Split the PDF into chunks of text
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator="/n"
    )
    document = loader.load()
    docs = text_splitter.split_documents(documents=document)

    # Summarize throught openai, use the chain_type specified
    llm = OpenAI(temperature=0)
    chain = load_summarize_chain(llm, chain_type=chain_type)
    openai_response = chain.run(docs)

    # todo: store the summary in a file

    return openai_response


if __name__ == "__main__":
    start = (
        time()
    )  # timing the method, because certain chain_types take a super long time

    print(
        summarize(
            pdf_path=args.file_path,
            chain_type=args.chain_type,
            chunk_overlap=args.chunk_overlap,
            chunk_size=args.chunk_size,
        )
    )

    print(f"Time to summarize using chain_type = {args.chain_type}: {time() - start}")
