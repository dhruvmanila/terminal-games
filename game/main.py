#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import string

# ---------------- public variables ----------------

# File containing the words, 
# words must be in separate lines
WORDLIST_FILENAME = "words.txt"

# Size of each hand
HAND_SIZE = 7

# Length of line separating the sections
LINE_SEP = '-' * 50

# ------------ end of public variables -------------

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print(f"{LINE_SEP}\nLoading word list from file...")
    with open(WORDLIST_FILENAME) as wordFile:
        wordList = []
        for line in wordFile:
            wordList.append(line.strip().lower())
    print(f"{len(wordList)} words loaded.\n{LINE_SEP}")
    return wordList


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary (string -> int)
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

	The score for a word is the product of two components:
	The first component is the sum of the points for letters in the word.
    (see SCRABBLE_LETTER_VALUES)
	The second component is the larger of:
        1, or
        (7 * wordlen) - (3 * (n - wordlen)), where wordlen is the length of the word and n is the hand length when the word was played.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower() # Only for testing
    letterPoints = sum([SCRABBLE_LETTER_VALUES[letter] for letter in word])
    otherPoints = (7 * len(word)) - (3 * (n - len(word)))
    bonusPoints = 1 if otherPoints < 1 else otherPoints
    totalPoints = letterPoints * bonusPoints
    return totalPoints


def display_hand(hand):
    """
    Returns the string in a displayable format.
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    letterString = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            letterString += letter + ' '
    return letterString


def deal_hand(n):
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
    hand={}
    numVowels = int(math.ceil(n / 3))

    for i in range(numVowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(numVowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    hand['*'] = 1
    return hand


def update_hand(hand, word):
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
    word = word.lower() # Only for testing
    newHand = dict(hand)
    for letter in word:
        if letter not in newHand:
            continue
        if newHand[letter] > 0:
            newHand[letter] -= 1
    return newHand
    

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    If the word contains the wildcard character '*', it makes a 
    list by replacing it with each vowels and searching the word
    in the word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower() # Only for testing
    for letter in word:
        if letter not in hand:
            return False
        elif letter == '*':
            wildWordList = [word.replace('*',v) for v in VOWELS]
            for wildWord in wildWordList:
                found = True if wildWord in word_list else False
                if found == True: break
            return found
        elif word.count(letter) > hand[letter]:
            return False
        
    return True if word in word_list else False


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum([num for num in hand.values()])


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand.

    NOTE:
    When any word is entered (valid or invalid), it uses up letters
    from the hand. An invalid word is rejected, and a message is displayed asking the user to choose another word.

    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: (int) total score for the hand
    """
    totalScore = 0

    while calculate_handlen(hand) > 0:
        print(f"\nCurrent hand: {display_hand(hand)}")
        playerInput = input('Enter word, or a "." to indicate that you are finished: ').lower()
        
        if playerInput == '.':
            break            
        
        elif is_valid_word(playerInput,hand,word_list):
            handLength = calculate_handlen(hand)
            playerInputScore = get_word_score(playerInput,handLength)
            totalScore += playerInputScore

            print(f'"{playerInput}" earned {playerInputScore} points. Total: {totalScore} points.')

        else:
            print("Invalid word, please try again.")

        hand = update_hand(hand,playerInput)
            
    if playerInput == '.':
        print(f"\nGame ended. Total score: {totalScore} points.\n")
    else:
        print(f"\nRan out of letters. Total score: {totalScore} points.\n")

    return totalScore


def substitute_hand(hand, letter):
    """ 
    Allows the user to replace all copies of one letter in the hand (chosen by user) with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter will be different from user's choice, and won't be any of the letters already in the hand. If user provides a letter not in the hand, the hand will be the same.

    Has no side effects: does not mutate hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    newHand = dict(hand)

    while letter in newHand:
        randLetter = random.choice(string.ascii_lowercase)
        if randLetter in newHand:
            continue        
        else:
            letterValue = newHand.pop(letter)
            newHand[randLetter] = letterValue
    
    return newHand


def readVal(valType, requestMsg, errorMsg="Invalid input."):
    '''
    valType: value type to return
    requestMsg: input prompt (exclude ':')
    errorMsg: error prompt

    returns value of type valType, handles exception
    '''
    while True:
        userInput = input(f"{requestMsg}: ")
        try:
            return (valType(userInput))
        except ValueError:
            print(f'"{userInput}": {errorMsg}\n')


def inputHandling(requestMsg, inputOption, errorMsg="Invalid input."):
    '''
    returns (str) user choice from the option and handles invalid input

    requestMsg (str): input prompt (exclude ':')
    inputOption (str/list): string/list containing the options
    errorMsg (str)(Optional): Default "Invalid input."

    NOTE: For str input, one string options only 
          otherwise input a list of options.
    '''
    optionList = list(inputOption)
    
    while True:
        userInput = input(f"{requestMsg}: ").lower()
        try:
            assert userInput in optionList
            return userInput
        except AssertionError:
            print(f'"{userInput}": {errorMsg}\n')


def play_game(word_list,numHands):
    """
    Allow the user to play a series of hands
    Returns the total score for the series of hands
    word_list: list of lowercase strings
    """
    totalSeriesCount = 0

    while numHands > 0:
        numHands -= 1
        hand = deal_hand(HAND_SIZE)
        print(f"{LINE_SEP}\nCurrent hand: {display_hand(hand)}")

        subChoice = inputHandling('Would you like to substitute a letter? [y/n]','yn')
        
        if subChoice == 'y':
            subLetter = inputHandling("Which letter would you like to replace",string.ascii_letters)
            hand = substitute_hand(hand,subLetter)
            handCount = play_hand(hand,word_list)
        else:
            handCount = play_hand(hand,word_list)
        
        replayChoice = inputHandling('Would you like to replay the hand? [y/n]','yn')

        if replayChoice == 'y':
            replayHandCount = play_hand(hand,word_list)
            handCount = replayHandCount if replayHandCount > handCount else handCount
        
        totalSeriesCount += handCount

    return totalSeriesCount

# --------------------- END OF MODULE --------------------- 

if __name__ == '__main__':
    word_list = load_words()

    choice = 'y'
    while choice == 'y':
        numHands = NH = readVal(int,"Enter total number of hands you want to play")
        seriesPoints = play_game(word_list,numHands)
        print(f"{LINE_SEP}\nTotal score over {NH} hands: {seriesPoints}\n{LINE_SEP}")
        choice = inputHandling("Do you want to play another series? [y/n]","yn")


