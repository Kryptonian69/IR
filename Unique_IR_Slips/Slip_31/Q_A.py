# Practical 31
# Source: IR_Question_16_April_2025_900_1100.pdf, Page 16
from Practical3_a import suggest_correction
def retrieve_information(query, dictionary):
    corrected_query = ' '.join([suggest_correction(word, dictionary) for word in query.split()])
    print(f"Retrieving for: '{corrected_query}'")
if __name__ == "__main__":
    dictionary = ["spelling", "correction", "algorithm", "information", "retrieval", "system"]
    retrieve_information("speling correctin algorithm", dictionary)
