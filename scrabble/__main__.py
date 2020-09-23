import os.path
import sys

try:
    import main
except ImportError:
    print(
        "Error: Could not start the game. Please make sure you're in the "
        "'terminal-games' directory."
    )
    sys.exit(1)

PATH = os.path.abspath(os.path.dirname(__file__))
main.WORDS_FILENAME = os.path.join(PATH, "words.json")
main.play()
