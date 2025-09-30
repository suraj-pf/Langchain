from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

chatmodel = ChatOpenAI(model="gpt-3.5-turbo",
                       temperature=2 # temperature is a parameter that affects the creativity and randomness of the model
                       ,max_completion_tokens=10
                       )  # Correct model name

result = chatmodel.invoke("What is the capital of India?")
print(result.content)  # Should print: "The capital of India is New Delhi."
# Note: Use result.content to access the text response from the chat model