from langchain_huggingface import HuggingFaceEmbeddings,HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

result = embedding.embed_query("Whats the capital of Maharashtra?")

print(str(result))


documents = [
    "Delhi is capital of India",
    "Mumbai is the business capital of India"
]

result = embedding.embed_documents(documents)

print(str(result))