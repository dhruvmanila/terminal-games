#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import random
from math import ceil
from string import ascii_lowercase
from typing import Iterable
from itertools import chain

# ---------------- public variables ----------------

# Size of each hand
HAND_SIZE = 7

# Length of line separating the sections
LINE_SEP = '-' * 50

# ------------ end of public variables -------------

WORDS_FILENAME = "words.json"

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}


def load_words() -> dict:
    """
    Returns a dictionary of valid words with keys being the length of the
    words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print(f"{LINE_SEP}\nLoading words from the file...")
    with open(WORDS_FILENAME) as word_file:
        word_dict = json.load(word_file)
    print(f"Words loaded. Game on!\n{LINE_SEP}")
    return word_dict


def get_word_score(word: str, n: int) -> int:
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the product of two components:
    The first component is the sum of the points for letters in the word.
    (see SCRABBLE_LETTER_VALUES)
    The second component is the larger of:
        1, or
        (7 * wordlen) - (3 * (n - wordlen)), where wordlen is the length
        of the word and n is the hand length when the word was played.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()  # Only for testing
    letter_points = sum([SCRABBLE_LETTER_VALUES[letter] for letter in word])
    other_points = (7 * len(word)) - (3 * (n - len(word)))
    bonus_points = 1 if other_points < 1 else other_points
    game_points = letter_points * bonus_points
    return game_points


def display_hand(hand: dict) -> str:
    """
    Returns the string in a displayable format.
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    letter_string = ''
    for letter in hand.keys():
        for _ in range(hand[letter]):
            letter_string += letter + ' '
    return letter_string


def deal_hand(n: int) -> dict:
    """
    Returns a random hand containing (n - 1) lowercase letters.
    ceil(n/3) letters in the hand are VOWELS.
    The last string is '*' as the wildcard in the game.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = int(ceil(n / 3))

    for _ in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for _ in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    hand['*'] = 1
    return hand


def update_hand(hand: dict, word: str) -> dict:
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand are ignored. Letters that appear in word more times
    than in hand doesn't result in a negative count; instead, sets the
    count in the returned hand to 0.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    word = word.lower()  # Only for testing
    new_hand = dict(hand)
    for letter in word:
        if letter not in new_hand:
            continue
        if new_hand[letter] > 0:
            new_hand[letter] -= 1
    return new_hand


def is_valid_word(word: str, hand: dict, word_dict: dict) -> bool:
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    If the word contains the wildcard character '*', it makes a
    list by replacing it with each vowels and searches the word
    in the word_list.

    word: string
    hand: dictionary (string -> int)
    word_dict: dictionary containing the words
    returns: boolean
    """
    word = word.lower()  # Only for testing
    word_length = str(len(word))
    if word_length == '1':
        return False

    for letter in word:
        if letter not in hand or word.count(letter) > hand[letter]:
            return False
        elif letter == '*':
            wild_word_list = [word.replace('*', v) for v in VOWELS]
            for wild_word in wild_word_list:
                if wild_word in word_dict[word_length]:
                    return True
            return False

    return True if word in word_dict[word_length] else False


def calculate_handlen(hand: dict) -> int:
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    return sum([num for num in hand.values()])


def comp_choose_word(hand: dict, word_dict: dict, n: int) -> str:
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.
    If no words in the wordList can be made from the hand, return None.
    """
    best_score = 0
    best_word = None
    # No need to loop over words of size longer than HAND_SIZE
    possible_words = list(word_dict.values())[:HAND_SIZE - 1]
    word_chain = chain(*possible_words)

    for word in word_chain:
        if is_valid_word(word, hand, word_dict):
            score = get_word_score(word, n)
            if score > best_score:
                best_score = score
                best_word = word

    return best_word


def comp_play_hand(hand: dict, word_dict: dict) -> int:
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.
    """
    comp_total_score = 0
    print(f"{LINE_SEP}\nComputer's game:")

    while (hand_length := calculate_handlen(hand)) > 0:
        print(f"\nCurrent hand: {display_hand(hand)}")
        comp_word = comp_choose_word(hand, word_dict, hand_length)

        if comp_word is None:
            break
        else:
            if not is_valid_word(comp_word, hand, word_dict):
                print('This is a terrible error! I need to check my own code!')
                break
            else:
                comp_score = get_word_score(comp_word, hand_length)
                comp_total_score += comp_score
                print(f'"{comp_word}" earned {comp_score} points. '
                      f'Total: {comp_total_score} points.')
        hand = update_hand(hand, comp_word)

    print(f"\nComputer game ended. Total score: {comp_total_score} points.\n")

    return comp_total_score


def play_hand(hand: dict, word_dict: dict) -> int:
    """
    Allows the user to play the given hand.

    NOTE:
    When any word is entered (valid or invalid), it uses up letters
    from the hand. An invalid word is rejected, and a message is displayed
    asking the user to choose another word.

    hand: dictionary (string -> int)
    returns: (int) total score for the hand
    """
    total_score = 0
    player_input = None

    while (hand_length := calculate_handlen(hand)) > 0:
        print(f"\nCurrent hand: {display_hand(hand)}")
        player_input = input('Enter word, or a "." to indicate '
                             'that you are finished: ').lower()

        if player_input == '.':
            break

        elif is_valid_word(player_input, hand, word_dict):
            player_input_score = get_word_score(player_input, hand_length)
            total_score += player_input_score

            print(f'"{player_input}" earned {player_input_score} points. '
                  f'Total: {total_score} points.')

        else:
            print("Invalid word, please try again.")

        hand = update_hand(hand, player_input)

    if player_input == '.':
        print(f"\nGame ended. Total score: {total_score} points.\n")
    else:
        print(f"\nRan out of letters. Total score: {total_score} points.\n")

    return total_score


def substitute_hand(hand: dict, letter: str) -> dict:
    """
    Allows the user to replace all copies of one letter in the hand
    (chosen by user) with a new letter chosen from the VOWELS and CONSONANTS
    at random. The new letter will be different from user's choice, and won't
    be any of the letters already in the hand. If user provides a letter not
    in the hand, the hand will be the same.

    Has no side effects: does not mutate hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_hand = dict(hand)

    while letter in new_hand:
        rand_letter = random.choice(ascii_lowercase)
        if rand_letter in new_hand:
            continue
        else:
            letter_value = new_hand.pop(letter)
            new_hand[rand_letter] = letter_value

    return new_hand


def read_val(val_type, request_msg: str, error_msg: str = "Invalid input."):
    """
    val_type: value type to return
    request_msg: input prompt (exclude ':')
    error_msg: error prompt

    returns value of type val_type, handles exception
    """
    while True:
        user_input = input(f"{request_msg}: ")
        try:
            return val_type(user_input)
        except ValueError:
            print(f'"{user_input}": {error_msg}\n')


def input_handling(request_msg: str, input_option: Iterable,
                   error_msg: str = "Invalid input.") -> str:
    """
    returns (str) user choice from the option and handles invalid input

    request_msg (str): input prompt (exclude ':')
    input_option (str/list): string/list containing the options
    error_msg (str)(Optional): Default "Invalid input."

    NOTE: For str input, one string options only
          otherwise input a list of options.
    """
    option_list = list(input_option)

    while True:
        user_input = input(f"{request_msg}: ").lower()
        try:
            assert user_input in option_list
            return user_input
        except AssertionError:
            print(f'"{user_input}": {error_msg}\n')


def play_game(num_hands: int, word_dict: dict) -> int:
    """
    Allow the user to play a series of hands
    Returns the total score for the series of hands
    """
    series_count = 0
    comp_series_count = comp_hand_count = 0
    replay_msg = 'Do you want to replay the hand? [y/n]'

    comp_choice = input_handling(
        'Do you want the computer to play against you? [y/n]', 'yn')

    while num_hands > 0:
        num_hands -= 1
        hand = deal_hand(HAND_SIZE)
        print(f"{LINE_SEP}\nCurrent hand: {display_hand(hand)}")

        sub_choice = input_handling('Do you want to substitute a letter? '
                                    '[y/n]', 'yn')

        if sub_choice == 'y':
            sub_letter = input_handling("Which letter would you like to "
                                        "replace?", ascii_lowercase)
            hand = substitute_hand(hand, sub_letter)

        hand_count = play_hand(hand, word_dict)

        if comp_choice == 'y':
            comp_hand_count = comp_play_hand(hand, word_dict)

            if comp_hand_count > hand_count:
                print(f"{LINE_SEP}\nComputer wins!\n")
                replay_msg = 'You have a change to redeem yourself. Do you want to replay the hand? [y/n]'
            else:
                print(f"{LINE_SEP}\nCongratulations! You beat the computer.\n")

        replay_choice = input_handling(replay_msg, 'yn')

        if replay_choice == 'y':
            replay_hand_count = play_hand(hand, word_dict)
            hand_count = replay_hand_count if replay_hand_count > hand_count \
                else hand_count

        series_count += hand_count
        comp_series_count += comp_hand_count

    return series_count, comp_series_count


# --------------------- END OF MODULE ---------------------


if __name__ == '__main__':
    WORD_DICT = load_words()
    total_series_points = 0
    comp_series_points = 0
    game_choice = 'y'

    while game_choice == 'y':
        total_hands = read_val(int, "Enter total number of hands "
                                    "you want to play")
        total_points, comp_total_points = play_game(total_hands, WORD_DICT)
        print(f"{LINE_SEP}\nTotal score over {total_hands} hands: "
              f"{total_points}\n{LINE_SEP}")
        game_choice = input_handling("Do you want to play another series? "
                                     "[y/n]", "yn")
        total_series_points += total_points
        comp_series_points += comp_total_points

    print(f"Thank you for playing.\n{LINE_SEP}")
