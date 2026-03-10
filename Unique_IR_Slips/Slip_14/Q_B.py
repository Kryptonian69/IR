# Practical 14
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 15
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = ['gold silver truck', 'shipment of gold damaged in a gold fire']
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("TF-IDF Matrix:\n", tfidf_matrix.toarray())
print("\nCosine Similarity Matrix:\n", cosine_similarities)
print("\nSimilarity between doc 0 and 1:", cosine_similarities[0, 1])
