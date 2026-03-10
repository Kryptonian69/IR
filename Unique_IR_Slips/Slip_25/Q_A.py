# Practical 25
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 9
import math

class VectorSpaceModel:
    def __init__(self, documents):
        self.documents = documents
        self.doc_vectors = self._calculate_tf_idf()

    def _calculate_tf_idf(self):
        tf_idf = {}
        total_docs = len(self.documents)
        
        # Calculate TF for each term in each document
        for doc_id, doc in self.documents.items():
            tf_idf[doc_id] = {}
            total_terms = len(doc)
            for term, freq in doc.items():
                tf = freq / total_terms
                
                # Calculate IDF
                doc_freq = sum(1 for document in self.documents.values() if term in document)
                idf = math.log(total_docs / (1 + doc_freq))
                
                # Calculate TF-IDF
                tf_idf[doc_id][term] = tf * idf
        return tf_idf

    def _normalize_vector(self, vector):
        norm = math.sqrt(sum(value ** 2 for value in vector.values()))
        if norm == 0: return vector
        return {term: value / norm for term, value in vector.items()}

    def _dot_product(self, vec1, vec2):
        return sum(vec1.get(term, 0) * vec2.get(term, 0) for term in set(vec1) | set(vec2))

    def cosine_similarity(self, query):
        query_vector = {}
        # Calculate TF for query terms
        total_terms = len(query)
        if total_terms == 0: return {doc_id: 0 for doc_id in self.doc_vectors}
        for term, freq in query.items():
            tf = freq / total_terms
            query_vector[term] = tf
            
            # Calculate TF-IDF for query terms
            total_docs = len(self.documents)
            doc_freq = sum(1 for document in self.documents.values() if term in document)
            idf = math.log(total_docs / (1 + doc_freq))
            query_vector[term] *= idf

        # Normalize query vector
        query_vector = self._normalize_vector(query_vector)

        # Compute cosine similarity between query and documents
        similarities = {}
        for doc_id, doc_vector in self.doc_vectors.items():
            similarities[doc_id] = self._dot_product(query_vector, doc_vector)
        return similarities

# Example usage
documents = {
    1: {'apple': 2, 'banana': 3},
    2: {'apple': 1, 'banana': 2, 'orange': 1},
    3: {'banana': 3, 'orange': 2}
}
vsm = VectorSpaceModel(documents)
query = {'apple': 1, 'banana': 1}
similarities = vsm.cosine_similarity(query)
print(similarities)