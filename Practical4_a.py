def calculate_metrics(retrieved, relevant):
    tp = len(retrieved & relevant)
    fp, fn = len(retrieved - relevant), len(relevant - retrieved)
    p = tp / (tp + fp) if (tp + fp) > 0 else 0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0
    f = 2 * p * r / (p + r) if (p + r) > 0 else 0
    return p, r, f

if __name__ == "__main__":
    p, r, f = calculate_metrics({"doc1", "doc2", "doc3"}, {"doc1", "doc4"})
    print(f"Precision: {p}\nRecall: {r}\nF-measure: {f}")
