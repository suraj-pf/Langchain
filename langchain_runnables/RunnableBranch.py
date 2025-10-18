from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough,RunnableBranch
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file (including GOOGLE_API_KEY)
load_dotenv() 

# Initialize the Chat Model. It automatically detects the GOOGLE_API_KEY from the environment.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model,parser)

branch_chain = RunnableBranch(
    # x:str
    (lambda x: len(x.split()) > 500,RunnableSequence(prompt2, model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)

result = final_chain.invoke({'topic':"Nigga"})

print(result)