
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Black hole'})
print(result)

# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.output_parsers import StrOutputParser
# from langchain.chains import SimpleChain

# # Load environment variables
# load_dotenv()

# # Initialize the model
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# # 1st prompt -> detailed report
# template1 = PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic']
# )

# # 2nd prompt -> summary
# template2 = PromptTemplate(
#     template='Write a 5 line summary on the following text: \n {text}',
#     input_variables=['text']
# )

# # Create a chain for generating the report
# detailed_report_chain = template1 | model

# # Create a chain for summarizing the report
# summary_chain = template2 | model

# # Run the chains
# detailed_report = detailed_report_chain.invoke({'topic': 'Black hole'})
# summary_result = summary_chain.invoke({'text': detailed_report})

# # Print the summary result
# print(summary_result)
