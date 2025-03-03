from stats import book_word_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        with open(sys.argv[1]) as f:
            text = f.read()
            word_count = book_word_count(text)
            each_letter = book_letter_count(text)
            reporting(each_letter, word_count)

#def book_word_count(text):
#    words = text.split()
#    total_words = 0
#
 #   for word in words:
  #      total_words += 1

   # return total_words

def book_letter_count(text):
    text_lowercased = text.lower()
    count_dict = {}

    for letter in text_lowercased:
        if letter in count_dict.keys():
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    return count_dict

def reporting(character_count, word_count):
    list_of_alpha = []

    for char in character_count.keys():
        if char.isalpha() == True:
            new_char = {"letter":char, "count": character_count[char]}
            list_of_alpha.append(new_char)

    list_of_alpha.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    #print(f"{word_count} words found in the document")
    print(f"Found {word_count} total words")
    print()
    for char in list_of_alpha:
        #print(f"The \'{char["letter"]}\' was found {char["count"]} times")
        print(f"{char["letter"]}: {char["count"]}")
    print("--- End report ---")
    return

def sort_on(dict):
    return dict["count"]

main()
