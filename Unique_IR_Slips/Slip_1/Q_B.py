# Practical 10b
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 1
from transformers import pipeline
def qa_system(): return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
if __name__ == "__main__":
    ctx = "Information retrieval is obtaining resources relevant to an information need. Searches can be full-text or content-based."
    qa = qa_system()
    print("Q: What can searches be based on?", qa(question="What can searches be based on?", context=ctx)['answer'])
