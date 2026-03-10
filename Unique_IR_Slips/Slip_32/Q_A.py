# Practical 32
# Source: IR_Question_16_April_2025_900_1100.pdf, Page 19
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus = ['The cat chased the dog around the garden', ' I read the book the night before']
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
df = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names_out())
print("DataFrame:\n", df)
alldata = df[(df['garden']==1) & (df['or']==1)]
print("AND query (this, first):", alldata.index.tolist())
ordata = df[(df['this']==1) | (df['first']==1)]
print("OR query (this, first):", ordata.index.tolist())
notdata = df[(df['and']!=1)]
print("NOT query (and):", notdata.index.tolist())
