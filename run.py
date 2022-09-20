import random 

class Color:
    """
    Sets colors to be called for different texts.
    """
    RESET = '\033[0m'
    BLUE = '\u001b[34m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\u001b[33m'

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
            if '_' not in correct_word:
                print("End me!")
                completed = True
            elif len(guess) != 1:
                print(f"\n{Color.YELLOW}Oops!, "
                      f"Your only allowed to guess {Color.RESET}1"
                  f" {Color.YELLOW}letter at a time.")
                print(f"You used {Color.RESET}{len(guess)} "
                      f"{Color.YELLOW}characters.\n{Color.RESET}")       
         elif guess in guessed_letters:
             print(f"\n{Color.YELLOW}You have already  used me"
             f" {Color.RESET}{guess}{Color.YELLOW}!{Color.RESET}")
             lives -= 1
         else: 
             print(f"\n{Color.GREEN}Great!! {Color.RESET}{guess}"
                   f" {Color.GREEN}is in the word! Keep going\n{Color.RESET}")    
         else:
             print('Please provide a single letter! Behave')
      if completed:
        win_graphic()
        print(f"{Color.GREEN}Well Done!"
              "You are a hero!")
    else:
        lose_graphic()
        print("Looks like you arent a hero, "
              "Do NOT quit your day job.")
        print(f"The word was: {Color.RESET}{word}{Color.RED}.{Color.RESET}")
    restart_game()
          



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
                # initial empty noose
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

