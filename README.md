# Terminal Games - MIT 6.0001

The old game of scrabble and hangman made as an assignment to the course
Introduction to Computer Science and Programming using Python. The game has
features combined from both the 
[edX](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/course/) 
version of the course and the 
[OCW fall 2016](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/index.htm) 
version. The game is simple and played on the terminal. Requirements and 
instructions are mentioned below.

## Instructions

Keep all the files and folders as it is in one folder. Download the game by 
one of the following ways:

Download the [zip file](https://github.com/dhruvmanila/scrabble/archive/master.zip) 

Download the folder from terminal: 
`git clone https://github.com/dhruvmanila/scrabble.git`

### How to open the game:

Open the terminal and go to the folder **hangman** or **scrabble** by entering
 the following command where directory path is the path to the folder from 
 your root directory. The first one is for Mac and the second is for Windows.

```
cd /users/username/path/to/gamename  -> For MacOS

cd C:\users\username\path\to\gamename  -> For Windows
```

Try running this command to get the list of the files `ls -l` and if you see
a file called **main.py** than you're in the correct folder otherwise
please google 'How to change directory from terminal in macOS/windows.'

To play the game enter the following command: `python3 main.py`

#### Words

There is a folder named 'Words' which contains all the json files from which 
I extracted the words. These files were available on the internet. I used the script
extract_words.py which is present in the folder to parse all the files in words_json folder
into a single file 'words.json' which is being used in both the games. Additionally,
if you want the words of different length, the files are present in the words_json folder.

## Scrabble

### How to play the game

If you know how to play scrabble then the rules for this one are pretty similar. 
At first you will be given the choice on how many hands you want to play. Then 
the computer will randomly create a hand and show it to you. Now you have a 
choice whether to substitute a letter from the given hand. If you type 'y' then 
you will be given the choice of which letter to substitute. You can only 
substitute one letter and it should be present in your hand.

There is a wildcard character " * " which can be used in place of any of the 
vowels. Enter the word in the input prompt. The computer will check whether 
the word is correct and compute the points and print it. There are over 175,393 
words in the json file. You can add additional words in the appropriate list
in the json file.

After playing one hand you will be given the choice to replay the hand if you 
were not satisfied. The highest score will be considered into the final score. 
After playing the desired number of hands, the total points will be computed 
and shown. You will be asked whether to play again or not. 

### Rules for the game

- For each hand you can substitute only once and replay the hand only once.
- " * " wildcard character can replace any of the vowels (a, e, i, o, u)
- Wrong inputs will be denied and error message will be shown.
- [y/n] inputs only take the letter "y" and "n"
- By default the number of letters in a hand are seven. To change the number see *additional instructions.*
- Letters entered randomly will be removed from the hand.

### Additional Instructions

If you want to change the number of letters in each hand or select a different 
file containing words you can do so by opening the **main.py** file in any text 
editor and edit the section with the heading **public variables**. Do not edit 
any of the things outside this boundary:

```
# ---------------- public variables ----------------

# Size of each hand
HAND_SIZE = 7

# Length of line separating the sections
LINE_SEP = '-' * 50

# ------------ end of public variables -------------
```

## Hangman

### How to play the game

Hangman is a game where one player thinks of a word, phrase or sentence and 
the other tries to guess it by suggesting letters within a certain number of 
guesses. The word to guess is represented by a row of dashes, representing 
each letter of the word.

The computer will inform you how long the word is. In each round you will be 
able to enter one letter as a guess. You will be shown how many letters are
available for you to guess. If you win the game, the computer will calculate 
the number of points. If you wish to play multiple games, the points
will accumulate.

#### Hints

There is a special symbol which you can type to get the hint. I could've
directly told you which symbol it is but then where's the fun in that and the
symbol is on your keyboard. You have 3 warnings to find out which symbol it 
is. You will only have one chance for calling the hint so make sure you call 
it at an appropriate time.

**Example:** For "a_ _ l_" the hints will be:

Possible word matches are:
addle adult agile aisle amble ample amply amyls angle
ankle apple apply aptly arils atilt

### Rules for the game
- At the start of each game you will be given 6 guesses and 3 warnings.
- Number of guesses will be cut when you input a wrong guess. 
(2 for vowels and 1 for consonants)
- Number of warnings will be cut if you input any digits or symbols 
(except for the hint symbol) and when you input the same letter again.

## Requirements
- Python version 3.x
- Terminal / Command line prompt

