# Practical 21
# Source: IR_Question_15_April_2025_1130_130.pdf, Page 6
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

class RankSVM:
    def __init__(self, model=SVC(kernel='linear')):
        self.model = model

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# Example usage
X, y = make_classification(n_samples=100, n_features=10, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
ranksvm = RankSVM()
ranksvm.fit(X_train, y_train)
print("Accuracy:", ranksvm.model.score(X_test, y_test))