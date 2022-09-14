import random 

def get_new_word():
    """
    Selects a random word from the words.txt file at the beginning of the game
    and ensures a new random word evry time the game is played.
    """
    with open('words.txt', 'r') as h:
        words = h.readlines()
    any_word = random.choice(words)[:-1].upper()
    return any_word