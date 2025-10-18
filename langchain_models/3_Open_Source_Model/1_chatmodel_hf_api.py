from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="model_here",
    task="text-generation",
) # type: ignore

model = ChatHuggingFace(llm=llm)

result  = llm.invoke("What is the capital of India?")

print(result)