# Practical 20
# Source: IR_Question_15_April_2025_1130_130.pdf, Page 1
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus = [" 'this is the first document", " 'this document is the second document", " 'And this is the third one", " 'Is this the first document?' and process the query “first and third”"]
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
df = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names_out())
print("DataFrame:\n", df)
alldata = df[(df['first']==1) & (df['third']==1)]
print("AND query (this, first):", alldata.index.tolist())
ordata = df[(df['this']==1) | (df['first']==1)]
print("OR query (this, first):", ordata.index.tolist())
notdata = df[(df['and']!=1)]
print("NOT query (and):", notdata.index.tolist())
