# Practical 18
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 19
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus = ['The university exam is scheduled next week']
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
df = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names_out())
print("DataFrame:\n", df)
alldata = df[(df['university']==1) & (df['mumbai']==1)]
print("AND query (this, first):", alldata.index.tolist())
ordata = df[(df['this']==1) | (df['first']==1)]
print("OR query (this, first):", ordata.index.tolist())
notdata = df[(df['and']!=1)]
print("NOT query (and):", notdata.index.tolist())
