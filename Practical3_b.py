from Practical3_a import suggest_correction
def retrieve_information(query, dictionary):
    corrected_query = ' '.join([suggest_correction(word, dictionary) for word in query.split()])
    print(f"Retrieving for: '{corrected_query}'")
if __name__ == "__main__":
    dictionary = ["spelling", "correction", "algorithm", "information", "retrieval", "system"]
    retrieve_information("speling correctin algorithm", dictionary)
