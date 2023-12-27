word_list = ['apple', 'banana', 'orange', 'grape', 'cherry']
print(word_list)

import random

word = random.choice(word_list)

print(word)

guess = input('Enter a letter')

def check_guess(guess):
  guess = guess.lower()     
  while True:
     if len(guess) == 1 and guess.isalpha() == True:
          break
     else:
          print("Invalid letter. Please, enter a single alphabetical character.")

check_guess(guess)
          
def ask_for_input():
   if guess  in word:
     print(f"Good guess! {guess} is in the word.")
   else:
     print(f"Sorry, {guess} is not in the word. Try again.")
     
ask_for_input()