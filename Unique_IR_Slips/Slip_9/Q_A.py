# Practical 9
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 10
def calculate_precision(retrieved_docs, relevant_docs):
    intersection = retrieved_docs.intersection(relevant_docs)
    return len(intersection) / len(retrieved_docs) if len(retrieved_docs) > 0 else 0

def calculate_recall(retrieved_docs, relevant_docs):
    intersection = retrieved_docs.intersection(relevant_docs)
    return len(intersection) / len(relevant_docs) if len(relevant_docs) > 0 else 0

def calculate_f_measure(precision, recall):
    return (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Example usage
retrieved_docs = {1, 2, 3, 4}
relevant_docs = {2, 3, 5}
precision = calculate_precision(retrieved_docs, relevant_docs)
recall = calculate_recall(retrieved_docs, relevant_docs)
f_measure = calculate_f_measure(precision, recall)

print("Precision:", precision)
print("Recall:", recall)
print("F-measure:", f_measure)