# Practical 7
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 8
import numpy as np
import re

class NaiveBayesClassifier:
    def __init__(self):
        self.vocab, self.pos_counts, self.neg_counts, self.p_prior, self.n_prior = [], None, None, 0, 0

    def preprocess(self, text): return re.findall(r'\b\w+\b', text.lower())

    def train(self, X, y):
        self.vocab = list(set([t for text in X for t in self.preprocess(text)]))
        self.pos_counts, self.neg_counts = np.zeros(len(self.vocab)), np.zeros(len(self.vocab))
        for text, label in zip(X, y):
            vec = np.zeros(len(self.vocab))
            for t in self.preprocess(text): vec[self.vocab.index(t)] += 1
            if label == 'positive': self.pos_counts += vec
            else: self.neg_counts += vec
        self.p_prior = sum(1 for label in y if label == 'positive') / len(y)
        self.n_prior = 1 - self.p_prior
        print("Model trained.")

if __name__ == "__main__":
    NaiveBayesClassifier().train(["The movie was amazing", "Terrible movie"], ["positive", "negative"])
