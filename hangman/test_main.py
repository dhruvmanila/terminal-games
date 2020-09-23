import pytest

from .main import (get_available_letters, get_guessed_word, is_word_guessed,
                   match_with_gaps)

TEST_IS_WORD_GUESSED = (
    ('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'], False),
    ('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'], True),
    ('pineapple', ['r', 'g', 'i', 'x', 'w', 'c', 'h', 'q', 'n', 'p'], False),
    ('mangosteen', ['g', 't', 'x', 'l', 'a', 'j', 'e', 'd', 'o', 'k'], False),
    ('grapefruit', [], False),
    ('carrot', ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't'], True),
)

TEST_GET_GUESSED_WORD = (
    ('apple', ['e', 'i', 'k', 'p', 'r', 's'], '_ pp_ e'),
    ('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'], 'durian'),
    ('carrot', ['l', 'q', 'z', 'n', 'h', 'g', 'u', 'y', 'b', 't'], '_ _ _ _ _ t'),
    ('grapefruit', ['p', 'g', 't', 'x', 'b', 'o', 'h', 'y', 'n', 'z'], 'g_ _ p_ _ _ _ _ t'),
    ('broccoli', [], '_ _ _ _ _ _ _ _ '),
    ('grapefruit', ['g', 'p', 'f', 'i', 'o', 's', 'm', 'j', 'v', 'w'], 'g_ _ p_ f_ _ i_ '),
)

TEST_GET_AVAILABLE_LETTERS = (
    (['e', 'i', 'k', 'p', 'r', 's'], 'abcdfghjlmnoqtuvwxyz'),
    ([], 'abcdefghijklmnopqrstuvwxyz'),
    (['b', 'm'], 'acdefghijklnopqrstuvwxyz'),
    (['c', 't', 's', 'y', 'j', 'd', 'r'], 'abefghiklmnopquvwxz'),
    (['t'], 'abcdefghijklmnopqrsuvwxyz'),
    (['z'], 'abcdefghijklmnopqrstuvwxy'),
)

TEST_MATCH_WITH_GAPS = (
    ('r_n_o_', 'random', True),
    ('a__l_', 'apple', True),
    ('t__t', 'test', True),
    ('b_n_na', 'letter', False),
)

@pytest.mark.parametrize("word, guessed, expected", TEST_IS_WORD_GUESSED)
def test_is_word_guessed(word, guessed, expected):
    assert is_word_guessed(word, guessed) == expected


@pytest.mark.parametrize("word, guessed, expected", TEST_GET_GUESSED_WORD)
def test_get_guessed_word(word, guessed, expected):
    assert get_guessed_word(word, guessed) == expected


@pytest.mark.parametrize("guessed, expected", TEST_GET_AVAILABLE_LETTERS)
def test_get_available_letters(guessed, expected):
    assert get_available_letters(guessed) == expected


@pytest.mark.parametrize("gap_word, word, expected", TEST_MATCH_WITH_GAPS)
def test_match_with_gaps(gap_word, word, expected):
    assert match_with_gaps(gap_word, word) == expected
