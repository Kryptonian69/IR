# Practical 16
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 2
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
    idx.add_document(1, "our class meeting starts soon")
    idx.add_document(2, "my class starts at 6.")
    idx.display()