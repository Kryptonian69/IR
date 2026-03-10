# Practical 34
# Source: IR_Question_16_April_2025_1130_130.pdf, Page 17
import numpy as np
import re
class NaiveBayesClassifier:
    def __init__(self): self.vocab, self.pos_counts, self.neg_counts, self.p_prior, self.n_prior = [], None, None, 0, 0
    def preprocess(self, text): return re.findall(r'\b\w+\b', text.lower())
    def vectorize(self, text):
        vec = np.zeros(len(self.vocab))
        for t in self.preprocess(text):
            if t in self.vocab: vec[self.vocab.index(t)] += 1
        return vec
    def train(self, X, y):
        self.vocab = list(set([t for text in X for t in self.preprocess(text)]))
        self.pos_counts, self.neg_counts = np.zeros(len(self.vocab)), np.zeros(len(self.vocab))
        for text, label in zip(X, y):
            if label == 'positive': self.pos_counts += self.vectorize(text)
            else: self.neg_counts += self.vectorize(text)
        self.p_prior = sum(1 for l in y if l == 'positive') / len(y)
        self.n_prior = 1 - self.p_prior
    def predict(self, X):
        preds = []
        for text in X:
            vec = self.vectorize(text)
            p_probs = (self.pos_counts + 1) / (sum(self.pos_counts) + len(self.vocab))
            n_probs = (self.neg_counts + 1) / (sum(self.neg_counts) + len(self.vocab))
            if np.sum(vec * np.log(p_probs)) + np.log(self.p_prior) > np.sum(vec * np.log(n_probs)) + np.log(self.n_prior): preds.append('positive')
            else: preds.append('negative')
        return preds
if __name__ == "__main__":
    clf = NaiveBayesClassifier()
    clf.train(["The movie was amazing, I like great acting", "Terrible! Would not recommend"], ['positive', 'negative'])
    y_test = ['positive']
    preds = clf.predict(["The acting was superb!"])
    acc = sum(1 for t, p in zip(y_test, preds) if t == p) / len(y_test)
    print(f"predicted class for the new review: {preds[0]}, accuracy: {acc}")
