# IR Viva Study Guide

## P1: Inverted Index
- **Goal:** Fast retrieval by mapping words to Document IDs.
- **Key Term:** Tokenization (splitting text into words).

## P2: Retrieval Models
- **Boolean:** Uses bitwise AND/OR/NOT logic on a term-matrix.
- **TF-IDF:** Weights words. TF = frequency in doc; IDF = rarity across all docs.
- **Cosine Similarity:** Measures the angle between query and document vectors (1.0 = identical).

## P3: Edit Distance
- **Levenshtein Distance:** Min. edits (insert, delete, replace) to match strings.
- **Usage:** Spelling correction and "Did you mean?" suggestions.

## P4: Evaluation Metrics
- **Precision:** Accuracy of results (Relevant retrieved / Total retrieved).
- **Recall:** Completeness of results (Relevant retrieved / Total relevant in existence).
- **F-Measure:** Harmonic mean of Precision and Recall.

## P5: Classification (Naive Bayes)
- **Goal:** Categorize text (e.g., Sentiment analysis: Positive/Negative).
- **Logic:** Uses probability based on word counts in training data.

## P6: Clustering (K-Means)
- **Goal:** Group similar documents automatically.
- **Silhouette Score:** Measures how well-defined the clusters are (-1 to 1).

## P7: Web Crawling
- **Goal:** Automated link following and data extraction.
- **Ethics:** Respect `robots.txt` and use delays to avoid crashing servers.

## P8: PageRank
- **Goal:** Measure page authority.
- **Logic:** A link from Page A to Page B is a "vote" for B's importance.

## P9: Learning to Rank
- **SVM:** Support Vector Machine used to learn ranking patterns.
- **MAP:** Mean Average Precision (Standard IR ranking metric).

## P10: Summarization & QA
- **Summarization:** Extracts high-scoring sentences based on word frequency.
- **QA System:** Uses Transformer models to find answers within a context paragraph.
