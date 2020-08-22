import json


def extract_words(to_file):
    for word_count in range(2, 16):
        with open(f"words_json/{word_count}_letter_words.json") as word_file:
            word_read = word_file.read()
            json_tree = json.loads(word_read)
            for word_dict in json_tree:
                word = word_dict['word']
                to_file.write(f"{word}\n")
        print(f"Done copying {word_count} letter words.")


if __name__ == "__main__":
    with open('words.txt', 'w') as main_word_file:
        extract_words(main_word_file)

'''Sample:
[
    {
        "word":"aa"
        },
    {
        "word":"ab"
        }
]
'''