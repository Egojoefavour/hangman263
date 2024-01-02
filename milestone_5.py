import random

class Hangman: # creating the Hangman class
    def __init__(self,  word_list, num_lives = 5 ):
      self.word = random.choice(word_list) #  The word to be guessed, picked randomly from the word_list
      self.word_guessed = [] #  list - A list of the letters of the word, with _ for each letter not yet guessed.
      self.num_letters = len(set(self.word)) #   int - The number of UNIQUE letters in the word that have not been guessed yet
      self.num_lives = num_lives # int - The number of lives the player has at the start of the game
      self.word_list = word_list # list of words
      self.list_of_guesses =  [] # a list of letters guessed so far
    
    
    def check_guess(self, guess):
      guess = guess.lower() # converts guess(alphabetical letter inputed) to lowercase lettters
      for letter in self.word:
        self.word_guessed.append("_") # create an unguessed, blank version of random word chosen
      if guess  in self.word:
       print(f"Good guess! {guess} is in the word.")
       for index, letter in  enumerate(self.word):
         if letter == guess:
          self.word_guessed[index] = letter # replaces the corresponding "_" in the word_guessed with the guess
         
       self.num_letters -= 1
      else:
       self.num_lives -= 1
       print(f"Sorry, {guess} is not in the word.")
       print(f"You have {self.num_lives} lives left.")
        
    def ask_for_input(self):
      while True:
       guess = input('Enter a letter') # letter guessed
       if len(guess) != 1 or guess.isalpha() == False: # Creates an if statement that runs if the guess is NOT a single alphabetical character
        print(f"Invalid letter. Please, enter a single alphabetical character.")
       elif guess in self.list_of_guesses:
        print("You already tried that letter!")
       else:
        self.check_guess(guess) # calling the check_guess method.
       self.list_of_guesses.append(guess) # creates a list of letters guessed so far
       break
      
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives) # creates an instance of the Hangman class and assigns it to game
    while True:
     if game.num_lives == 0: # Checks if the num_lives is 0
      print('You lost!')
      break
     if game.num_letters >= 0:# checks if the num_letters is greater than 0
      game.ask_for_input() # calling the ask_for_input() method to continue the game
     if  game.num_lives != 0 and  game.num_letters  <= 0: # creates an if statement that runs if num_lives is not 0 and the num_letters is not greater than 0, which means the user has won the game
      print('Congratulations. You won the game!')
      break
play_game(['apple', 'banana', 'orange', 'grape', 'cherry']) # calling the play_game function to play the game
    

            