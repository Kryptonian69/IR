# Practical 7
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 8
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus = ['BSc lectures start at 7', 'My lectures are over', ' Today is a holiday']
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
df = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names_out())
print("DataFrame:\n", df)
alldata = df[(df['not']==1) & (df['lectures']==1)]
print("AND query (this, first):", alldata.index.tolist())
ordata = df[(df['this']==1) | (df['first']==1)]
print("OR query (this, first):", ordata.index.tolist())
notdata = df[(df['and']!=1)]
print("NOT query (and):", notdata.index.tolist())
