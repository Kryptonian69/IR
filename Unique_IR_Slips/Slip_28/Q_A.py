# Practical 28
# Source: IR_Question_16_April_2025_900_1100.pdf, Page 1
def levenshtein_distance(str1, str2):
    len_str1, len_str2 = len(str1) + 1, len(str2) + 1
    matrix = [[0 for _ in range(len_str2)] for _ in range(len_str1)]
    for i in range(len_str1): matrix[i][0] = i
    for j in range(len_str2): matrix[0][j] = j
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            cost = 0 if str1[i-1] == str2[j-1] else 1
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost)
    return matrix[len_str1-1][len_str2-1]

def suggest_correction(word, word_list):
    return min(word_list, key=lambda w: levenshtein_distance(word, w))

if __name__ == "__main__":
    dictionary = ["hello", "world", "python", "spell", "correct", "algorithm"]
    print(f"Correction for 'helo': {suggest_correction('helo', dictionary)}")
