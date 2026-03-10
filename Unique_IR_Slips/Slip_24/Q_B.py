# Practical 24
# Source: IR_Question_15_April_2025_1130_130.pdf, Page 11
from collections import defaultdict
import re

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def add_document(self, doc_id, text):
        words = self._preprocess(text)
        for word in words:
            self.index[word].add(doc_id)

    def _preprocess(self, text):
        # Tokenization
        words = re.findall(r'\b\w+\b', text.lower())
        # Stopword Removal (can be expanded)
        stopwords = {'a', 'an', 'the', 'is', 'are', 'in', 'on', 'at', 'to', 'for', 'of'}
        words = [word for word in words if word not in stopwords]
        # Stemming or Lemmatization (optional)
        # Add stemming or lemmatization algorithm here if needed
        return words

    def search(self, query):
        words = self._preprocess(query)
        result = set()
        for word in words:
            if word in self.index:
                result |= self.index[word] # Union of sets
        return result

# Example usage
index = InvertedIndex()
index.add_document(1, "This is a sample document")
index.add_document(2, "Another document for testing")
index.add_document(3, "Yet another example document")
print(index.search("sample document"))