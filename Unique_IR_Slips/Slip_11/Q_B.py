# Practical 11
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 12
def calculate_metrics(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0
    f = 2 * p * r / (p + r) if (p + r) > 0 else 0
    return p, r, f

if __name__ == '__main__':
    p, r, f = calculate_metrics(60, 30, 20)
    print(f'Precision: {p}\nRecall: {r}\nF-measure: {f}')