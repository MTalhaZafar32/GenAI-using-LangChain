from langchain_huggingface import HuggingFaceEmbeddings


embedding =  HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text = "I am a undergrad of datascience"
vector = embedding.embed_query(text)

print(str(vector))