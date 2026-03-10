# Practical 34
# Source: IR_Question_16_April_2025_1130_130.pdf, Page 17
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