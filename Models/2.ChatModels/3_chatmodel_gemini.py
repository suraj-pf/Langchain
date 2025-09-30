from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from a .env file (including GOOGLE_API_KEY)
load_dotenv() 

# Ensure the GOOGLE_API_KEY is available
if not os.getenv("GOOGLE_API_KEY"):
    # This check is added for robustness, although load_dotenv should handle it.
    print("Error: GOOGLE_API_KEY environment variable not found.")
    # Exit or raise error if the key is missing
    exit()

# Initialize the Chat Model. It automatically detects the GOOGLE_API_KEY from the environment.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Invoke the model to generate content
result = model.invoke("Write a poem about the sea.")

# Print the final generated content
print(result.content)
