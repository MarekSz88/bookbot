from stats import *
import sys

def printNicelyAlphabetCharacters(unique_chars):
    for char in unique_chars:
        if(char.isalpha()):
            print(f"The {char}: {unique_chars[char]} character was found times")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return 1

    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {book_path} ---")
        counted_words = countWords(file_contents)
        print(f"{counted_words} words found in the document\n")
        printNicelyAlphabetCharacters(countUniqueChars(file_contents))        

main()
    