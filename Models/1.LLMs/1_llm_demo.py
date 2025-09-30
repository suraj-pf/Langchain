from langchain_openai import OpenAI # Import the OpenAI LLM from langchain_openai
from dotenv import load_dotenv # Used to load environment variables from a .env file

load_dotenv() # Load environment variables from a .env file 

# LLM are inherited from BaseLLM models
llm = OpenAI(model="gpt-3.5-turbo-instruct") # You can specify any model available in OpenAI

result = llm.invoke("What is the capital of India") # the invoke method is used to call the model and get the response

print(result) # Should print "The capital of India is New Delhi."