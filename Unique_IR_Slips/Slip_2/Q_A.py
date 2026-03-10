# Practical 1
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 2
import re
from collections import defaultdict
class DocumentRetrievalSystem:
    def __init__(self):
        self.index = defaultdict(set)
        self.documents = {}
    def tokenize(self, text): return re.findall(r'\b\w+\b', text.lower())
    def index_document(self, doc_id, text):
        self.documents[doc_id] = text
        for token in self.tokenize(text): self.index[token].add(doc_id)
    def retrieve_documents(self, query):
        tokens = self.tokenize(query)
        relevant_doc_ids = set()
        for token in tokens:
            if token in self.index:
                if not relevant_doc_ids: relevant_doc_ids.update(self.index[token])
                else: relevant_doc_ids.intersection_update(self.index[token])
        return [(doc_id, self.documents[doc_id]) for doc_id in relevant_doc_ids]
if __name__ == "__main__":
    doc_retrieval = DocumentRetrievalSystem()
    doc1 = "The quick brown fox jumped over the lazy dog"
    doc2 = "The lazy dog slept in the sun"
    doc_retrieval.index_document("document1", doc1)
    doc_retrieval.index_document("document2", doc2)
    query = "lazy sun"
    results = doc_retrieval.retrieve_documents(query)
    print("Query:", query)
    for doc_id, text in results: print(f"Document {doc_id}: {text}")
