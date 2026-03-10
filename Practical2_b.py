from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = ["This is a sample document.", "Another document for testing.", "A third document to demonstrate the vector space model."]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("TF-IDF Matrix:\n", tfidf_matrix.toarray())
print("\nCosine Similarity Matrix:\n", cosine_similarities)
print("\nSimilarity between doc 0 and 1:", cosine_similarities[0, 1])
