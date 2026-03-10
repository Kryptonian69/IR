# Practical 7
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 8
class BooleanRetrieval:
    def __init__(self, index):
        self.index = index

    def boolean_search(self, query):
        query = query.lower()
        terms = query.split()

        if 'and' in terms:
            intersection = None
            for term in terms:
                if term != 'and':
                    if intersection is None:
                        intersection = self.index.get(term, set())
                    else:
                        intersection &= self.index.get(term, set())
            return intersection if intersection is not None else set()

        elif 'or' in terms:
            union = set()
            for term in terms:
                if term != 'or':
                    union |= self.index.get(term, set())
            return union

        elif 'not' in terms:
            complement = self.index.keys()
            for term in terms:
                if term != 'not':
                    complement -= self.index.get(term, set())
            return complement
        else:
            return self.index.get(query, set())

# Example usage
index = {
    'apple': {1, 2, 3},
    'banana': {2, 3, 4},
    'orange': {3, 4, 5}
}
boolean_retrieval = BooleanRetrieval(index)
print(boolean_retrieval.boolean_search("apple and banana"))