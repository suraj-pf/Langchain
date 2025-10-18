from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file (including GOOGLE_API_KEY)
load_dotenv() 

# Initialize the Chat Model. It automatically detects the GOOGLE_API_KEY from the environment.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6)


loader = TextLoader("cricket.txt", encoding="utf-8")
docs = loader.load()


print(docs,type(docs),len(docs),sep="\n")

print(docs[0].page_content)
print(docs[0].metadata)


prompt = PromptTemplate(
    template="Write a summary of following poem \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))