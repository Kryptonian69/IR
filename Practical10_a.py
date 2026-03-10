import nltk
nltk.download('punkt_tab', quiet=True)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt', quiet=True); nltk.download('punkt_tab', quiet=True); nltk.download('stopwords', quiet=True)
def summarize(text):
    sw, words = set(stopwords.words("english")), word_tokenize(text)
    freq = {}
    for w in words:
        w = w.lower()
        if w.isalnum() and w not in sw: freq[w] = freq.get(w, 0) + 1
    sentences = sent_tokenize(text)
    s_val = {s: sum(freq.get(w.lower(), 0) for w in word_tokenize(s)) for s in sentences}
    avg = sum(s_val.values()) / len(s_val)
    return " ".join([s for s in sentences if s_val[s] > 1.2 * avg])
if __name__ == "__main__":
    txt = "Information retrieval is obtaining resources relevant to an information need. Searches can be full-text or content-based. IR is the science of searching documents and metadata. IR systems reduce information overload. Web search engines are visible IR applications."
    print("Summary:", summarize(txt))
