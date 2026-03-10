import re
from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

    def add_document(self, doc_id, text):
        tokens = self.tokenize(text)
        for token in tokens:
            self.index[token].add(doc_id)

    def display(self):
        print("Inverted Index:")
        for token, doc_ids in sorted(self.index.items()):
            print(f"'{token}': {sorted(list(doc_ids))}")

if __name__ == "__main__":
    idx = InvertedIndex()
    idx.add_document(1, "This is the first document")
    idx.add_document(2, "This is the second document")
    idx.add_document(3, "Another document is here")
    idx.display()
