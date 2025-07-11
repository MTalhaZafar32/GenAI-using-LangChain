from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "LangChain is a powerful framework for building applications using LLMs with external data sources.",
    "OpenAI provides powerful APIs like GPT-4 and text-embedding-3 for building generative AI apps.",
    "HuggingFace Transformers offer a wide range of open-source models for NLP and computer vision tasks.",
    "Vector databases like Pinecone and FAISS are used to store and retrieve document embeddings efficiently.",
    "Fine-tuning models helps developers customize LLM behavior for domain-specific tasks."
]

query = 'how to use vector db with llm'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)
