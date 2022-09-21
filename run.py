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


def introduction_page():
    """
    The initial introduction to the hangman game.
    The player can select to read the instuctions or begin the game straight away.
    """    
    word = get_new_word()
    hangman_sign()
    print(hangman_construction(0))
    print(f"Type {Color.BLUE}1 {Color.RESET} to start the game\n")
    print(f"Type {Color.BLUE}2 {Color.RESET} if you would like to read the instructions")
    selection = False 
    while not selection:
        decision = input("\n")
        if decision == "1":
            selection = True
            begin_game(word)
        elif decision == "2":
            selection = True
            game_instructions()
        else:
            print(f"\n{Color.YELLOW}Please type {Color.BLUE}1 {Color.YELLOW}or"
                  f"{Color.BLUE} 2 {Color.YELLOW}to make your decision."
                  f"{Color.RESET}")

              
def game_instructions():
    """
    Gives the player the instructions to play the game. 
    """
    print(
        """
        The object of the game is to guess the word.
        Do this by entering in one letter each go.
        If you enter a wrong letter a life will be taken from you.
        If you lose all your lives, say goodbye to the hanging individual.
        Guess the word before your lives hit 0 and you are a hero.
        """
    )

    begin = ("Press the enter key to begin the game.\n")
    introduction_page()    
    


def begin_game(word):
    """
    Starts the game for the user 
    checks if the letter the player inputs is in the hidden word.
    if the letter is correct,game will iterate through hidden word and letter will go into
    correct position. if incorrect,a message will be relayed to the user.
    player can see how many lives are left to complete the game.
    
    """
    correct_word = "_" * len(word)
    completed = False
    guessed_letters = []
    lives = 6 
    print("Help Me!!!\n")
    print(f"Lives left {lives}\n")
    while completed is not True: 
        print(correct_word)
        guess = input('Give me some letters please \n')
        if len(guess) == 1 and guess.isalpha(
        ) and guess not in guessed_letters:
            guessed_letters.append(guess)
            word_list = list(correct_word)
            indices = [
               i for i, letter in enumerate(word) if letter == guess.upper()
            ]
            for index in indices:
                word_list[index] = guess
                correct_word = "".join(word_list)
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
        elif guess not in word:
            print(f"\n{Color.YELLOW}Oh no! {Color.RESET}{guess}"
            f"{Color.YELLOW} isn't in the word!\n{Color.RESET}")
            lives -= 1
            guessed_letters.append(guess)    
        else: 
            print(f"\n{Color.GREEN}Great!! {Color.RESET}{guess}"
            f" {Color.GREEN}is in the word! Keep going\n{Color.RESET}")
    if completed:
        win_sign()
        print(f"{Color.GREEN}Well Done!"
              "You are a hero!")
    else:
        lose_sign()
        print("Looks like you arent a hero, "
              "Do NOT quit your day job.")
        print(f"The word was: {Color.RESET}{word}{Color.RED}.{Color.RESET}")
    start_game_again()
    
    
    
def start_game_again():
    """
    Asks if the user wants to start the game again.
    If not, returns to main screen.
    """
    start_again_option = input(f"\nWould you like to try again? "
                           f"{Color.BLUE}Y{Color.RESET}/{Color.BLUE}N\n"
                           f"{Color.RESET}").upper()
    if start_again_option == "Y":
        word = get_new_word()
        begin_game(word)
    elif start_again_option == "N":
        introduction_page()
    else:
        print(f"{Color.YELLOW}Time to decide {Color.BLUE}Y {Color.YELLOW}"
              f"or {Color.BLUE}N{Color.YELLOW}. You chose "
              f"{Color.RESET}{start_again_option}{Color.YELLOW}.{Color.RESET}\n")
        start_game_again()

def hangman_construction(lives):

    """
    Shows the user how man lives are left before the games ends.
    """
    stages = [
        f"""
              =======
              |/    |
              |     {Color.RED}@{Color.RESET}
              |    /|\\
              |     |
              |    / \\
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     {Color.RED}@{Color.RESET}
              |    /|\\
              |     |
              |    /
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     {Color.RED}@{Color.RESET}
              |    /|\\
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     {Color.RED}@{Color.RESET}
              |    /|
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     {Color.RED}@{Color.RESET}
              |     |
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     {Color.RED}@{Color.RESET}
              |
              |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |
              |
              |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """
    ]
    return stages[lives]


def hangman_sign():
    """
    A title graphic to be displayed on the title screen.
    """
    print(
        """
          ██╗  ██╗█████╗███╗   ██╗██████╗███╗   ███╗█████╗███╗   ██╗
          ██║  ████╔══██████╗  ████╔════╝████╗ ██████╔══██████╗  ██║
          ████████████████╔██╗ ████║  █████╔████╔███████████╔██╗ ██║
          ██╔══████╔══████║╚██╗████║   ████║╚██╔╝████╔══████║╚██╗██║
          ██║  ████║  ████║ ╚████╚██████╔██║ ╚═╝ ████║  ████║ ╚████║
          ╚═╝  ╚═╚═╝  ╚═╚═╝  ╚═══╝╚═════╝╚═╝     ╚═╚═╝  ╚═╚═╝  ╚═══                                                                                   
        """
    )


def win_sign():
    """
    Displays a win sign for when the player correctly guesses the word
    to let them know they were correct.
    """
    print(
          f"""{Color.GREEN}
     :::       ::: ::::::::::: ::::    ::: 
    :+:       :+:     :+:     :+:+:   :+:  
   +:+       +:+     +:+     :+:+:+  +:+   
  +#+  +:+  +#+     +#+     +#+ +:+ +#+    
 +#+ +#+#+ +#+     +#+     +#+  +#+#+#     
#+#+# #+#+#      #+#     #+#   #+#+#      
###   ###   ########### ###    ####  
            
        {Color.RESET}"""
        )


def lose_sign():
    """
    Displays a lose sign for when the player fails to guess the word
    to let them know the lost the game.
    """
    print(
          f"""{Color.RED}
            ::::::::::   :::     ::::::::::: :::  
           :+:        :+: :+:       :+:     :+:   
          +:+       +:+   +:+      +:+     +:+    
         :#::+::#  +#++:++#++:     +#+    +#+     
        +#+       +#+    +#+     +#+     +#+      
       #+#      #+#     #+#     #+#     #+#       
      ###      ###      ### ########### ########## 
        {Color.RESET}"""
        )


introduction_page()