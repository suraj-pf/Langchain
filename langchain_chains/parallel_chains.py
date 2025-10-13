from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

# Load environment variables
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the text \n {text}"
    ,input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate multiple choice quiz from the text \n {text}"
    ,input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the notes and the quiz into a single document \n ntoes-> {notes} and quiz -> {quiz}"
    ,input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallechain = RunnableParallel({
    'notes' : prompt1 | model | parser,
    'quiz' : prompt2 | model | parser
})
# chain = prompt1 | model | parser | prompt2 | model | parser | prompt3 | model | parser
merge_chain =  prompt3 | model | parser
 
chain = parallechain | merge_chain

text = """
Supply chain management (SCM) is the process of overseeing and coordinating all activities involved in a product's journey, from raw materials to the final customer. This includes sourcing, production, logistics, and distribution, with the goal of improving efficiency, reducing costs, and enhancing customer satisfaction. Effective SCM requires the integration of processes, data, and financial flows across all partners, from suppliers to manufacturers to retailers. 
Key components of supply chain management
Sourcing: Procuring raw materials and components from suppliers.
Production: Transforming raw materials into finished goods.
Logistics: Managing the movement of goods, which includes transportation and warehousing.
Inventory Management: Optimizing the amount of inventory to meet demand while minimizing storage costs.
Demand Planning: Forecasting and planning for the demand of products or services.
Distribution: The movement of finished products to customers.
Return Management: Handling the return of excess or defective products. 
Goals of supply chain management
Improve efficiency: Streamlining processes to reduce waste and delays.
Reduce costs: Finding ways to lower expenses throughout the supply chain.
Enhance customer value: Ensuring products are available to customers when and where they are needed.
Gain a competitive advantage: Using an optimized supply chain to outperform competitors. 
Importance of collaboration
Effective SCM requires partners throughout the chain—suppliers, manufacturers, distributors, and retailers—to work together.
Collaboration is crucial for managing risk, improving inventory visibility, and adapting to changes in the market. 
"""

result = chain.invoke({"text":text})

print(result)

chain.get_graph().print_ascii()