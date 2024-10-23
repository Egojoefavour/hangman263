word_list = ['apple', 'banana', 'orange', 'grape', 'cherry']
import random

class Hangman:
    def __init__(self,  word_list, num_lives = 5 ):
      self.word = random.choice(word_list)
      self.word_guessed = list('_'*len(self.word))
      print(self.word_guessed)
      self.num_letters = len(set(self.word))
      self.num_lives = num_lives
      self.word_list = word_list
      self.list_of_guesses =  []
    
    
    def check_guess(self, guess):
      
      if guess.lower()  in self.word:
       print(f"Good guess! {guess} is in the word.")
       for index, letter in enumerate(self.word):
        if self.word[index] == guess:
         self.word_guessed[index] = letter
         print(self.word_guessed)
       self.num_letters -= 1
      else:
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")
        
    def ask_for_input(self):
      while True:
       guess = input('Enter a letter')
       if len(guess) != 1 and guess.isalpha() == False:
        print(f"Invalid letter. Please, enter a single alphabetical character.")
       elif guess in self.list_of_guesses:
        print("You already tried that letter!")
       else:
        self.check_guess(guess)
        self.list_of_guesses.append(guess)
             
love = Hangman(word_list)
love.ask_for_input()    
            