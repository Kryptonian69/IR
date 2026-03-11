from sklearn.metrics import average_precision_score, recall_score, f1_score, precision_score
y_true = [0, 1, 1, 0, 1, 1]
y_scores = [0.1, 0.4, 0.35, 0.8, 0.65, 0.91]
y_pred = [1 if score >= 0.5 else 0 for score in y_scores]
print(f'Average precision-recall score: {average_precision_score(y_true, y_scores)}')
print(f'Average precision-recall score: {recall_score(y_true, y_pred)}')
print(f'Average precision-recall score: {f1_score(y_true, y_pred)}')
print(f'Average precision-recall score: {precision_score(y_true, y_pred)}')