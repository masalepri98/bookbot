from collections import Counter
import string

def main():
    path_to_file = 'books/frankenstein.txt'
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
            # Count the number of words in the file
            word_count = count_words(file_contents)
            # Count character occurrences
            char_occurrences = count_character_occurrences(file_contents)
            # Generate and print the report
            print_report(path_to_file, word_count, char_occurrences)
    except FileNotFoundError:
        print(f"The file at {path_to_file} was not found.")
    except IOError:
        print(f"An error occurred while reading the file at {path_to_file}.")

def count_words(text):
    """Returns the number of words in the given text."""
    words = text.split()
    return len(words)

def count_character_occurrences(text):
    """Returns a dictionary with the count of each character in the given text, case-insensitive."""
    text = text.lower()
    return Counter(text)

def print_report(file_path, word_count, char_occurrences):
    """Prints a formatted report of word and character counts."""
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    # Filter and sort character occurrences for alphabetic characters only
    for char in string.ascii_lowercase:
        if char in char_occurrences:
            print(f"The '{char}' character was found {char_occurrences[char]} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()