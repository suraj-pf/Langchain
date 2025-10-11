from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

# prompt = template.invoke({'topic':'blackhole'})

# result = model.invoke(prompt)

# print("RAW output:\n", result.content)

# try:
#     print("PARSED output:\n", parser.parse(result.content))
# except Exception as e:
#     print("Parsing failed:\n", e)

"""
RAW output:
 ```json
{
        "fact_1": "Black holes are regions in spacetime where gravity is so strong that nothing, not even light, can escape once it crosses a certain boundary called the event horizon."
        "fact_2": "They are typically formed from the remnants of massive stars (at least several times the mass of our Sun) that collapse under their own gravity at the end of their life cycle."
        "fact_3": "Despite their name, black holes are not empty space; they contain an immense amount of matter packed into an incredibly small area, giving them their powerful gravitational pull."
}
```
Parsing failed:
 Got invalid JSON object. Error: Expecting ',' delimiter: line 3 column 2 (char 182)
For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/OUTPUT_PARSING_FAILURE 
((venv) ) suraj@Surajs-MacBook-Air output_parser % 

Missing commas between "fact_1" and "fact_2", etc. So the JSON is invalid.
"""
