from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

message = HumanMessage(content="As a Generative AI Engineer in 2025, list and describe 7 powerful tools or platforms that are currently popular for building Generative AI applications. For each tool, briefly mention its use case, such as prototyping chatbots, building RAG pipelines, model fine-tuning, or deploying AI apps.")
response = chat_model.invoke([message])
print(response.content)
