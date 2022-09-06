from haystack import Pipeline, JoinDocuments
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import FilterRetriever

document_store_1 = InMemoryDocumentStore()
retriever_1 = FilterRetriever(document_store_1, scale_score = True)
# add content to retriever
dicts_1 = [
  {
    'content': "Alpha",
    'score': 0.5
  }
]
document_store_1.write_documents(dicts_1)

document_store_2 = InMemoryDocumentStore()
retriever_2 = FilterRetriever(document_store_2, scale_score = True)
# add content to retriever
dicts_2 = [
  {
    'content': "Beta",
    'score': 0.5
  }
]
document_store_2.write_documents(dicts_2)


document_store_3 = InMemoryDocumentStore()
retriever_3 = FilterRetriever(document_store_3, scale_score = True)
# add content to retriever
dicts_3 = [
  {
    'content': "Gamma",
  }
]
document_store_3.write_documents(dicts_3)


document_store_4 = InMemoryDocumentStore()
retriever_4 = FilterRetriever(document_store_4, scale_score = True)
# add content to retriever
dicts_4 = [
  {
    'content': "Delta",
  }
]
document_store_4.write_documents(dicts_4)


documents = retriever_1.retrieve(query="Alpha Beta Gamma Delta")
print(documents)
for doc in documents:
  print(doc)


pipeline = Pipeline()
pipeline.add_node(component=retriever_1, name="Retriever1", inputs=["Query"])
pipeline.add_node(component=retriever_2, name="Retriever2", inputs=["Query"])
pipeline.add_node(component=JoinDocuments(join_mode="concatenate"), name="Join12", inputs=["Retriever1", "Retriever2"])


res = pipeline.run(query="Alpha Beta Gamma Delta")
print(res)
documents = res['documents']
for doc in documents:
  print(doc)

