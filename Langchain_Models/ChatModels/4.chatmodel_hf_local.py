from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=1000
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("As a Generative AI Engineer in 2025, list and describe 7 powerful tools or platforms that are currently popular for building Generative AI applications. For each tool, briefly mention its use case, such as prototyping chatbots, building RAG pipelines, model fine-tuning, or deploying AI apps")

print(result.content)