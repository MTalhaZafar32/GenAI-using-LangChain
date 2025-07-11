from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions= 32)

documents= [
 "As a Generative AI Engineer in 2025",
 "list and describe 7 powerful tools or platforms that are currently popular for building Generative AI applications.",
 "For each tool, briefly mention its use case, such as prototyping chatbots, building RAG pipelines, model fine-tuning, or deploying AI apps"
]

result = embedding.embed_documents(documents)
print(str(result))
