# Practical 11
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 12
from transformers import pipeline

# Load the pre-trained question-answering model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Sample text passage
context = "The Pyramids of Egypt were built as tombs for pharaohs. They are located near Cairo."
questions = ["What were the Pyramids built for?", "Where are they located?"]

# Answer the questions
for question in questions:
    result = qa_pipeline(question=question, context=context)
    print(f"Question: {question}")
    print(f"Answer: {result['answer']}\n")