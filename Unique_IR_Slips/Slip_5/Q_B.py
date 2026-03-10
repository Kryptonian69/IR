# Practical 5
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 5
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def extractive_summarize(text, num_sentences=2):
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    if not sentences: return ""
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
    sentence_scores = cosine_similarities.mean(axis=1)
    top_indices = np.argsort(sentence_scores)[-num_sentences:]
    summary = [sentences[i] for i in sorted(top_indices)]
    return '. '.join(summary)

# Example usage
text = "Natural language processing is a field of AI. It involves interactions between computers and humans. Summarization is a common task."
print("--- Extractive Summary ---")
print(extractive_summarize(text))