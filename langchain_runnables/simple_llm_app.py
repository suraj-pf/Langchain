from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts  import PromptTemplate

# Load environment variables from a .env file (including GOOGLE_API_KEY)
load_dotenv() 

# Initialize the Chat Model. It automatically detects the GOOGLE_API_KEY from the environment.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

prompt = PromptTemplate(
    template= "",
    input_variables=['Suggest a catchy blog title about {topic}']
)
topic = input('Suggest a topic:- ')

formated_prompt = prompt.format(topic=topic)

blog_title = model.invoke(formated_prompt)

print("Generated blog title is",blog_title)