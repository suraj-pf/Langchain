from langchain_community.document_loaders import CSVLoader
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6)

loader = CSVLoader(file_path="Social_Network_Ads.csv")

docs = loader.load()

print(len(docs))
print(docs[0])