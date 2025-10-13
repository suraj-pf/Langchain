from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

# Load environment variables
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt1 = PromptTemplate(
    template="Classify the following feedback text into positive or negative \n {feedback}"
    ,input_variables=['feedback']
)

# prompt2 = PromptTemplate(
#     template="Generate multiple choice quiz from the text \n {text}"
#     ,input_variables=['text']
# )

# prompt3 = PromptTemplate(
#     template="Merge the notes and the quiz into a single document \n ntoes-> {notes} and quiz -> {quiz}"
#     ,input_variables=['notes','quiz']
# )

parser = StrOutputParser()

classifier_chain = prompt1 | model | parser

print(classifier_chain.invoke({'feedback': 'This is a terrible smartphone' }))