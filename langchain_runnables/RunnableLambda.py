from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file (including GOOGLE_API_KEY)
load_dotenv() 

# Initialize the Chat Model. It automatically detects the GOOGLE_API_KEY from the environment.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)

def word_count(text):
    return len(text.split()) 

# runnable_word_counter = RunnableLambda(word_count) 

# result = runnable_word_counter.invoke('Hi there how are you myself suraj more')

# print(result)

prompt1 = PromptTemplate(
    template="Generate a joke on {topic}",
    input_variables=['topic']
)

pasrer = StrOutputParser()

joke_generator_chain = RunnableSequence(prompt1 | model | pasrer)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'word_count' : RunnableLambda(word_count)
        # 'word count' : RunnableLambda(lambda x : len(x.split()))
    }
)

chain = RunnableSequence(joke_generator_chain | parallel_chain)


result = chain.invoke({'topic':"AI"})

print(f"the joke is {result['joke']}")
print(f" word count is :- {result['word_count']}")