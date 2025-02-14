def countUniqueChars(string):
    unique_chars = {}
    for char in string.lower():
        if char in unique_chars:
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars

def printNicelyAlphabetCharacters(unique_chars):
    for char in unique_chars:
        if(char.isalpha()):
            print(f"The '{char}' character was found {unique_chars[char]} times")

def countWords(string):
    words = string.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        counted_words = countWords(file_contents)
        print(f"{counted_words} words found in the document\n")
        printNicelyAlphabetCharacters(countUniqueChars(file_contents))        

main()
    