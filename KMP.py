def compute_border(pattern):
    m = len(pattern)
    border = [0] * m
    j = 0

    # i starts from 1 since border[0] is always 0
    for i in range(1, m):
        while (j > 0 and pattern[i] != pattern[j]):
            j = border[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
            border[i] = j
        else:
            border[i] = 0

    return border

def kmpSearch(pattern, text):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0  # Immediate match if pattern is empty

    border = compute_border(pattern)
    j = 0  # index for pattern

    # i is the index for text
    for i in range(n):
        while (j > 0 and text[i] != pattern[j]):
            j = border[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            return i - m + 1  # Match found at index i - m + 1

        # If we've reached the end of text and no match was found
        if i == n - 1 and j != m:
            return -1

    return -1  # Pattern not found

# print(kmpSearch("hski","ski"))

