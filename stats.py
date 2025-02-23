def countUniqueChars(string):
    unique_chars = {}
    for char in string.lower():
        if char in unique_chars:
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars

def countWords(string):
    words = string.split()
    return len(words)