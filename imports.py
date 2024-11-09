# Basic utilities
import os
from dotenv import load_dotenv

# Web scraping
import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import BSHTMLLoader

# LangChain core
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Vector operations
from langchain.text_splitter import RecursiveJsonSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.chains import RetrievalQA