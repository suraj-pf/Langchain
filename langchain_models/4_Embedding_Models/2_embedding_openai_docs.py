from langchain_openai import OpenAIEmbeddings,OpenAI
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-small',
    dimensions=32
)

documents = [
    "Delhi is capital of India",
    "Mumbai is the business capital of India"
]

result = embedding.embed_documents(documents)

print(str(result))