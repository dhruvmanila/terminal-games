"""
There are JSON files in the words_json folder containing words of different
length which I got from the internet. This script is used to parse all the
files into a list and converting that into a python dictionary where the
keys are the length of words and the values are all the words in a list of
same length. This dictionary is stored in words.json file for later use.

Sample:
[
    {
        "word":"aa"
        },
    {
        "word":"ab"
        }
]
"""
import json
from string import ascii_lowercase


def extract_words(to_file):
    word_dict = {}
    for word_count in range(2, 16):
        with open(f"words_json/{word_count}_letter_words.json") as word_file:
            json_tree = json.load(word_file)
            for json_dict in json_tree:
                word = json_dict['word']
                word_code = str(len(word)) + word[0]
                if word_code not in word_dict:
                    word_dict[word_code] = [word]
                else:
                    word_dict[word_code].append(word)
        if len(word_dict) != (26 * (word_count - 1)):
            for letter in ascii_lowercase:
                check = str(word_count) + letter
                _ = word_dict.setdefault(check, [])
        print(f"Done copying {word_count} letter words.")

    json.dump(word_dict, to_file)


if __name__ == "__main__":
    with open('words.json', 'w') as main_word_file:
        extract_words(main_word_file)
