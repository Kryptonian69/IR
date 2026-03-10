# Practical 30
# Source: IR_Question_16_April_2025_900_1100.pdf, Page 14
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, fowlkes_mallows_score

# Example labels
ground_truth_labels = [0, 1, 1, 0, 2, 2, 2, 3, 3, 3]
cluster_labels = [1, 0, 0, 1, 2, 2, 2, 3, 3, 3]

# Compute evaluation metrics
ari = adjusted_rand_score(ground_truth_labels, cluster_labels)
nmi = normalized_mutual_info_score(ground_truth_labels, cluster_labels)
fmi = fowlkes_mallows_score(ground_truth_labels, cluster_labels)

# Print evaluation metrics
print("Adjusted Rand Index (ARI):", ari)
print("Normalized Mutual Information (NMI):", nmi)
print("Fowlkes-Mallows Index (FMI):", fmi)