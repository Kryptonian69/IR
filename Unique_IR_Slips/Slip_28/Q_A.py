# Practical 28
# Source: IR_Question_16_April_2025_900_1100.pdf, Page 1
class SpellingCorrector:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def _edit_distance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                       dp[i][j - 1],      # Insertion
                                       dp[i - 1][j - 1]) # Substitution
        return dp[m][n]

    def correct_spelling(self, word):
        min_distance = float('inf')
        corrected_word = word
        for vocab_word in self.vocabulary:
            distance = self._edit_distance(word, vocab_word)
            if distance < min_distance:
                min_distance = distance
                corrected_word = vocab_word
        return corrected_word

# Example usage
vocabulary = {'apple', 'banana', 'orange', 'grape', 'kiwi'}
corrector = SpellingCorrector(vocabulary)
print(f"Correction for 'appl':", corrector.correct_spelling('appl'))