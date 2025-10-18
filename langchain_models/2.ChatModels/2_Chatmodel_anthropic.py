from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# Use the correct model name
model = ChatAnthropic(model="claude-3-5-sonnet-20240620")

# Invoke the model
result = model.invoke("Hello, how are you?")

# Print response correctly
print(result.content)
