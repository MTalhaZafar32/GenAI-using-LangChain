from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature= 0.1 , max_completion_tokens= 12)

result = model.invoke("Which city is called the city of Nawabs in Pakistan?")

print(result.content)
