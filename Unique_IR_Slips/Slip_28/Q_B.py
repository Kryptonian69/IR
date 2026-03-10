# Practical 28
# Source: IR_Question_16_April_2025_900_1100.pdf, Page 1
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
documents = [
    "Machine learning is the study of computer algorithms that improve automatically through experience.",
    "Deep learning is a subset of machine learning.",
    "Natural language processing is a field of artificial intelligence.",
    "Computer vision is a field of study that enables computers to interpret and understand the visual world.",
    "Reinforcement learning is a type of machine learning algorithm that teaches an agent how to make decisions in an environment by rewarding desired behaviors.",
    "Information retrieval is the process of obtaining information from a collection of documents.",
    "Text mining is the process of deriving high-quality information from text.",
    "Data clustering is the task of dividing a set of objects into groups.",
    "Hierarchical clustering builds a tree of clusters.",
    "K-means clustering is a method of vector quantization."
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
k = 3
kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
kmeans.fit(X)
print(f"Silhouette Score: {silhouette_score(X, kmeans.labels_)}")
for i in range(k):
    print(f"\nCluster {i+1}:")
    for idx in np.where(kmeans.labels_ == i)[0]:
        print("-", documents[idx])
