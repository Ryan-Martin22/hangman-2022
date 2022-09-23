# Hangman 2022 - Hangman Game 

## Introduction 

Hangman 2022 is a classic Hangman game. The object of the game is to guess the hidden word before your lives run out, thus hanging the man/woman. The hidden word is randomly selected from a list of alomost one thousand words. You can play this game anythime and anywhere as you dont need an opposing player in order to play the game. 

The game can be found [**here**](https://hangman-2022.herokuapp.com/)

![Title Sceen](assets/images/Main-screen.png)

# Features 

## Existing Features 

### Landing page 

* The first things the user sees when entering the game is a visual representation of a the Hangman logo and also an image of the hangman itself. This is eyecatching and fun for the user to see. 
* The user is also presented with two options, to either start the game immediately or view the game instructions. 4

![Title Sceen](assets/images/Main-screen.png)

### Instructions 

* If the user decides he or she would like to view the game instructions before beginning, the user must type 2. He or she is then presented with the game instructions. 
* After viewing the game instructions the user just has to hit Enter to continue to the main game. 

![Instructions](assets/images/instructions.png)

### Start Game

* When the user types 1 to start the game, he or she is brought to the main game page. 
* On this page the user is shown an empty hangimng struture, his or her lives, and also a blank worf structure.
* The user is prompted to type in some letters to save the hangman. 

![Start of game](assets/images/start.png)

### Correct Guess 

* When the user inputs a correct guess, he or she will be freeted with a green message telling them it was correct.
* No lives will be taken from the user and the hangman structure will remain empty. 

![Correct Guess](assets/images/Correct-guess.png)

### Wrong Guess 
 
* If the user whilst playing the game enters a wrong guess, the hangman will start to form from the head downwards and the user will ne told in yellow that the guess was incorrect.The head will be coloured red for better UX. 
* The user will also be shown that he or she has lost a life. 
* The user will also be show the letters that have been already guessed to prevent the user from guessing the same letter. 

![Wrong Guess](assets/images/wrong-guess.png)

### Guessed the same letter 

* If the user guesses a letter he or she has already guessed, he or she will be shown a message stating that fact and also what letter the have guessed already. 
* No lives will be taken from the user and the hangman will remain the same. The message is presented in yellow to avt as a warning to the user. 

![Already Guessed](assets/images/already-guessed.png)



