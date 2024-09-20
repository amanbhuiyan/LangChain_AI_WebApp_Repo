from PyPDF2 import PdfReader

# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

from langchain.text_splitter import CharacterTextSplitter

# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS


from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI

# from langchain_community.llms import OpenAI
from langchain_openai import OpenAI


import os

from dotenv import load_dotenv

load_dotenv()


# provide the path of  pdf file/files.
pdfreader = PdfReader('C:/Everything/Projects/Python Projects/LagnChain_AI_Web_App/Data/magic.pdf')


from typing_extensions import Concatenate
# read text from pdf
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content


# print(raw_text)

# We need to split the text using Character Text Split such that it sshould not increse token size
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

# print(len(texts))


# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()


document_search = FAISS.from_texts(texts, embeddings)

document_search

# print(document_search)

chain = load_qa_chain(OpenAI(), chain_type="stuff")



query = "What is a footnote?"
docs = document_search.similarity_search(query)

input_data= {

    'input_documents': docs,
    'question': query,
}

print("=================================================================")
# print(chain.run(input_documents=docs, question=query))

# print(chain.invoke(input=input_data))

print(chain.invoke(input=input_data)['output_text'])


