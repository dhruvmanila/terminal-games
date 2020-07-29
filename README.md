# Scrabble [MIT 6.0001]

The old game of scrabble made as an assignment to the course Introduction to Computer Science and Programming using Python. The game has features combined from both the edX version of the course and the OCW fall 2016 version. The game is simple and played on the terminal. Requirements and instructions are mentioned below.

## Instructions

Keep all the files and folders as it is in one folder. Download the game by one of the following ways:

Download the [zip file](https://github.com/dhruvmanila/scrabble/archive/master.zip) 

Download the folder from terminal: `git clone https://github.com/dhruvmanila/scrabble.git`

### How to open the game:

Open the terminal and go to the folder **GAME** by entering the following command where directory path is the path to the folder from your root directory. The first one is for Mac and the second is for Windows.

`cd /users/username/somefolder/GAME`

`cd C:\users\username\somefolder\GAME`

Try running this command to get the list of the files `ls -l` and if you see a file called **main.py** than you're in the correct folder otherwise please google 'How to change directory from terminal.'

To play the game enter the following command: `python3 main.py`

### How to play the game

If you know how to play scrabble then the rules for this one are pretty similar. At first you will be given the choice on how many hands you want to play. Then the computer will randomly create a hand and show it to you. Now you have a choice whether to substitute a letter from the given hand. If you type 'y' then you will be given the choice of which letter to substitute. You can only substitute one letter and it should be present in your hand.

After that you can create words and press enter. The computer will check whether the word is correct and compute the points and print it. There are over 175,393 words in the file. If you want to add another word you can add it in words.txt file. **THE WORD SHOULD BE ADDED IN A NEWLINE.**

After playing one hand you will be given the choice to replay the hand if you were not satisfied. The highest score will be considered into the final score.

### Rules for the game

- For each hand you can substitute only once and replay the hand only once.
- Wrong inputs will be denied and error message will be shown.
- By default the number of letters in a hand are seven. To change the number see *additional instructions.*
- Letters from random words entered will be removed from the hand.

### Additional Instructions

If you want to change the number of letters in each hand or select a different file containing words you can do so by opening the main.py file in any text editor and edit the section with the heading **public variables**. Do not edit any of the things outside this boundary.

## Requirements
- Python version 3.x
- Terminal / Command line prompt

