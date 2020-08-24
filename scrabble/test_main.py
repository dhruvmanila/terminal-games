#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from .main import get_word_score, update_hand, is_valid_word, load_words

WORD_DICT = load_words()

TEST_SCORE = [
    ("", 7, 0),
    ("it", 7, 2),
    ("was", 7, 54),
    ("weed", 6, 176),
    ("scored", 7, 351),
    ("WaYbILl", 7, 735),
    ("Outgnaw", 7, 539),
    ("fork", 7, 209),
    ("FORK", 4, 308),
    ("h*ney", 7, 290),  # with wilcards
    ("c*ws", 6, 176),  # with wilcards
    ("wa*ls", 7, 203)  # with wilcards
]

TEST_UPDATE_HAND = [
    ({'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}, "quail",
     {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}),
    ({'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}, "Evil",
     {'e': 0, 'v': 1, 'n': 1, 'i': 0, 'l': 1}),
    ({'h': 1, 'e': 1, 'l': 2, 'o': 1}, "HELLO",
     {'h': 0, 'e': 0, 'l': 0, 'o': 0})
]

TEST_VALID_WORD = [
    ({'h': 1, 'e': 1, 'l': 2, 'o': 1}, "hello", True),
    ({'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}, "Rapture", False),
    ({'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}, "Honey", True),
    ({'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}, "honey", False),
    ({'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}, "EVIL", True),
    ({'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}, "Even", False)
]

TEST_WILDCARD = [
    ({'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}, "e*m", False),
    ({'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}, "honey", False),
    ({'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}, "h*ney", True),
    ({'c': 1, 'o': 1, '*': 1, 'w': 1, 's': 1, 'z': 1, 'y': 2}, "c*wz", False),
]


@pytest.mark.parametrize('word, n, expected', TEST_SCORE)
def test_get_word_score(word, n, expected):
    score = get_word_score(word, n)
    assert score == expected


@pytest.mark.parametrize('handorig, word, expected', TEST_UPDATE_HAND)
def test_update_hand(handorig, word, expected):
    handcopy = handorig.copy()
    outcome = update_hand(handcopy, word)
    assert outcome == expected
    assert handcopy == handorig, "Implementation mutated the original hand."


@pytest.mark.parametrize('handorig, word, expected', TEST_VALID_WORD)
def test_is_valid_word(handorig, word, expected):
    handcopy = handorig.copy()
    outcome = is_valid_word(word, handcopy, WORD_DICT)
    assert outcome == expected
    assert handcopy == handorig, "Implementation mutated the original hand."


@pytest.mark.parametrize('handorig, word, expected', TEST_WILDCARD)
def test_wildcard(handorig, word, expected):
    handcopy = handorig.copy()
    outcome = is_valid_word(word, handcopy, WORD_DICT)
    assert outcome == expected
    assert handcopy == handorig, "Implementation mutated the original hand."
