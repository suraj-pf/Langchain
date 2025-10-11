from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
import os

# 1. Load environment variables from a .env file (e.g., GOOGLE_API_KEY)
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

st.header('Reasearch Tool')


# Input for selecting research paper name
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Select...",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

# Input for selecting explanation style
style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

# Input for selecting explanation length
length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Define the template with placeholders for inputs
template = load_prompt('Prompts/template.json')
prompt = template.invoke({
                'paper_input' : paper_input,
                'style_input': style_input,
                'length_input' : length_input
}
                
)

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        
                'paper_input' : paper_input,
                'style_input': style_input,
                'length_input' : length_input
    })
    result = model.invoke(prompt) # type : ignore
    st.write(result.content) # type : ignore