# Practical 29
# Source: IR_Question_16_April_2025_900_1100.pdf, Page 2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
def evaluate(docs, k=3):
    X = TfidfVectorizer().fit_transform(docs)
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X)
    return km.labels_, silhouette_score(X, km.labels_)
if __name__ == "__main__":
    docs = ["Machine learning is computer algorithms.", "Deep learning is subset of ML.", "NLP is AI field.", "CV is field of study.", "Clustering is grouping objects.", "Hierarchical clustering builds trees."]
    labels, score = evaluate(docs, k=2)
    print("Labels:", labels, "Score:", score)
