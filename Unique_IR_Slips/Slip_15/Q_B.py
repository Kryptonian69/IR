# Practical 15
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 16
from sklearn.metrics import average_precision_score
y_true = [0, 1, 1, 0, 1, 1]
y_scores = [0.1, 0.4, 0.35, 0.8, 0.65, 0.91]
print(f'Average precision-recall score: {average_precision_score(y_true, y_scores)}')
