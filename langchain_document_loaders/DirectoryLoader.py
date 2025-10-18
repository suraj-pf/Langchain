from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file (including GOOGLE_API_KEY)
load_dotenv() 

# Initialize the Chat Model. It automatically detects the GOOGLE_API_KEY from the environment.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6)

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(docs)
print(type(docs))
print(len(docs))


docs = loader.lazy_load()

for document in docs:
    print(document.metadata)