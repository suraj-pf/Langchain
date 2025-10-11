from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Dict,TypedDict
import os

# Load environment variables from a .env file (including GOOGLE_API_KEY)
load_dotenv() 

class Review(TypedDict):
    summary: str
    sentiment: str

# Initialize the Chat Model. It automatically detects the GOOGLE_API_KEY from the environment.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
# model = ChatOpenAI()

# Use the dataclass as a schema for structured output
structured_model = model.with_structured_output(Review)

# Invoke the model to generate content
result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

# Print the final generated content
print(result)
