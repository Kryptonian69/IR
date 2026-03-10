# Practical 28
# Source: IR_Question_16_April_2025_900_1100.pdf, Page 1
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Prepare Your Document Data
data = ["Machine learning is great", "Natural language processing is a field of AI", "Clustering is unsupervised"]

# Step 2: Vectorize the Documents
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data)

# Step 3: Choose a Clustering Algorithm
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# Step 4: Train the Clustering Algorithm
kmeans.fit(X)

# Step 5: Evaluate the Clustering Results
if len(set(kmeans.labels_)) > 1:
    silhouette_avg = silhouette_score(X, kmeans.labels_)
    print("Silhouette Score:", silhouette_avg)
print("Labels:", kmeans.labels_)