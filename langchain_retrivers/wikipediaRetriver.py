from langchain_community.retrievers import WikipediaRetriever
from yarl import Query

retriever = WikipediaRetriever(top_k_results=2,lang="en")

query = "the geopolitical history of india and pakistan from the perspective of a chinese"

docs = retriever.invoke(query)

for i,doc in enumerate(docs):
    print(f"----Result {i+1}-----")
    print(f"----Content {i+1} \n {doc} \n-----")
