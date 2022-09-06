from haystack import Pipeline, JoinDocuments
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import FilterRetriever

document_store_1 = InMemoryDocumentStore()
retriever_1 = FilterRetriever(document_store_1, scale_score = True)
# add content to retriever
dicts_1 = [
  {
    'content': "Alpha",
    'score': 0.55
  }
]
document_store_1.write_documents(dicts_1)

document_store_2 = InMemoryDocumentStore()
retriever_2 = FilterRetriever(document_store_2, scale_score = True)
# add content to retriever
dicts_2 = [
  {
    'content': "Beta",
    'score': 0.54
  }
]
document_store_2.write_documents(dicts_2)


document_store_3 = InMemoryDocumentStore()
retriever_3 = FilterRetriever(document_store_3, scale_score = True)
# add content to retriever
dicts_3 = [
  {
    'content': "Gamma",
    'score': 0.53
  }
]
document_store_3.write_documents(dicts_3)


document_store_4 = InMemoryDocumentStore()
retriever_4 = FilterRetriever(document_store_4, scale_score = True)
# add content to retriever
dicts_4 = [
  {
    'content': "Delta",
    'score': 0.51
  }
]
document_store_4.write_documents(dicts_4)


documents = retriever_1.retrieve(query="Alpha Beta Gamma Delta")
for doc in documents:
  print(doc)
documents = retriever_2.retrieve(query="Alpha Beta Gamma Delta")
for doc in documents:
  print(doc)
documents = retriever_3.retrieve(query="Alpha Beta Gamma Delta")
for doc in documents:
  print(doc)
documents = retriever_4.retrieve(query="Alpha Beta Gamma Delta")
for doc in documents:
  print(doc)


pipeline = Pipeline()
pipeline.add_node(component=retriever_1, name="Retriever1", inputs=["Query"])
pipeline.add_node(component=retriever_2, name="Retriever2", inputs=["Query"])
pipeline.add_node(component=retriever_3, name="Retriever3", inputs=["Query"])
pipeline.add_node(component=retriever_4, name="Retriever4", inputs=["Query"])
pipeline.add_node(component=JoinDocuments(), name="Join12", inputs=["Retriever1", "Retriever2"])
pipeline.add_node(component=JoinDocuments(), name="Join34", inputs=["Retriever3", "Retriever4"])
pipeline.add_node(component=JoinDocuments(), name="JoinFinal", inputs=["Join12", "Join34"])


res = pipeline.run(query="Alpha Beta Gamma Delta")
print(res)
documents = res['documents']
for doc in documents:
  print(doc)

