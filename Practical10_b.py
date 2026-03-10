from transformers import pipeline
def qa_system(): return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
if __name__ == "__main__":
    ctx = "PageRank was named after Larry Page, a Google founder. It ranks web pages by counting link quantity and quality."
    qa = qa_system()
    print("Q: Who?", qa(question="Who was PageRank named after?", context=ctx)['answer'])
    print("Q: How?", qa(question="How does it rank pages?", context=ctx)['answer'])
