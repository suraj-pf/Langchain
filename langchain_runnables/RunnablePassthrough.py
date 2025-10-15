# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
# from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

# load_dotenv()

# prompt1 = PromptTemplate(
#     template='Write a joke about {topic}',
#     input_variables=['topic']
# )

# model = ChatOpenAI()

# parser = StrOutputParser()

# prompt2 = PromptTemplate(
#     template='Explain the following joke - {text}',
#     input_variables=['text']
# )

# joke_gen_chain = RunnableSequence(prompt1, model, parser)

# parallel_chain = RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'explanation': RunnableSequence(prompt2, model, parser)
# })

# final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# print(final_chain.invoke({'topic':'cricket'}))

from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file (including GOOGLE_API_KEY)
load_dotenv() 

# Initialize the Chat Model. It automatically detects the GOOGLE_API_KEY from the environment.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt1 = PromptTemplate(
    template="Generate a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the following joke \n {text}",
    input_variables=['text']
)

pasrer = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "Joke" : RunnablePassthrough(),
        'Explanation' : RunnableSequence(prompt2 | model | pasrer)
    }
)

joke_generator_chain = RunnableSequence(prompt1 | model | pasrer)

chain = RunnableSequence(joke_generator_chain | parallel_chain)

result = chain.invoke({'topic':"AI"})

print(result)