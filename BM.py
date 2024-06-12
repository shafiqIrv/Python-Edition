def LastOccurrence(pattern):
    last = [-1] * 128  # Assuming ASCII character set
    for index in range(len(pattern)):
        last[ord(pattern[index])] = index
    return last

def bmSearch(pattern, text):
    last = LastOccurrence(pattern)
    n = len(text)
    m = len(pattern)
    i = m - 1  # Start at the end of the pattern, 
               # aligned with corresponding position in text

    while i < n:
        j = m - 1  # Start comparison at the end of the pattern
        while j >= 0 and pattern[j] == text[i]:
            j -= 1
            i -= 1
        if j < 0:  # If all characters matched
            return i + 1  # Match found, return starting index
        else:
            i += m - min(j, 1 + last[ord(text[i])])  # Shift the pattern

    return -1  # No match found


