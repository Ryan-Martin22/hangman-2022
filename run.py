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


def begin_game(word):
    """
    Starts the game for the user

    """
    correct_word = "_" * len(word)
    completed = False
    guessed_letters = []
    guessed_words = []
    lives = 6 
    print("Help Me!!!\n")
    print(f"Lives left {lives}\n")
    print(word)
    while completed is not True: 
        print(correct_word)
        guess = input('Give me some letters please \n')
        if len(guess) == 1 and guess.isalpha(
        ) and guess not in guessed_letters:
            guessed_letters.append(guess)
            word_list = list(correct_word)
            indices = [
               i for i, letter in enumerate(word) if letter == guess.upper{}
            ]
            for index in indices:
               word_list[index] = guess
            correct_word= "".join(word_list)
            if '_' not in correct_word
                print("End me!")
                completed = True
         elif guess in guessed_letters:
             print('You have already used me')
         else:
             print('Please provide a single letter! Behave')
    print("You Win!")      



def hangman_construction(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]

