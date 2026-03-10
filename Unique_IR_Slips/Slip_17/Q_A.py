# Practical 17
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 18
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = ['The sun is the star at the center of the solar system.', 'She wore a beautiful dress to the party last night.', 'The book on the table caught my attention immediately.']
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("TF-IDF Matrix:\n", tfidf_matrix.toarray())
print("\nCosine Similarity Matrix:\n", cosine_similarities)
print("\nSimilarity between doc 0 and 1:", cosine_similarities[0, 1])
