from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
X, y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train, X_test = sc.fit_transform(X_train), sc.transform(X_test)
model = SVC(kernel='linear').fit(X_train, y_train)
preds = (model.decision_function(X_test) > 0).astype(int)
print("Accuracy:", accuracy_score(y_test, preds))
