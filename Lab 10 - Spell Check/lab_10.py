import re


def split_line(line):
    # split function
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def linear_search(words, dictio_list):
    # linear search
    words = words.upper()
    for dict_word in dictio_list:
        if dict_word == words:
            return True
    return False


def binary_search(words, dictio_list):
    # binary search
    key = "Spell Check"
    low = 0
    high = len(dictio_list) - 1
    words = words.upper()
    while low <= high:
        mid = (low + high) // 2
        if dictio_list[mid] == words:
            return True
        elif dictio_list[mid] < words:
            low = mid + 1
        else:
            high = mid - 1
    return False


def main():

    # Reading the dictionary into array
    dictionary_file = open("dictionary.txt", "r")
    dictionary_list = [line.strip().upper() for line in dictionary_file]
    dictionary_file.close()

    # Linear Search
    print("--- Linear Search ---")
    alice_file = open("AliceInWonderLand200.txt", "r")
    line_number = 0
    for line in alice_file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            if not linear_search(word, dictionary_list):
                print(f"Line {line_number} Possible misspelled word: {word}")
    alice_file.close()

    # Binary Search
    print("--- Binary Search ---")
    alice_file = open("AliceInWonderLand200.txt", "r")
    line_number = 0
    for line in alice_file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            if not binary_search(word, dictionary_list):
                print(f"Line {line_number} Possible misspelled word: {word}")

    alice_file.close()


main()
