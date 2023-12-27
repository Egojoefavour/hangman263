word_list = ['apple', 'banana', 'orange', 'grape', 'cherry']
print(word_list)

import random

word = random.choice(word_list)
print(word)

guess = input('Enter a letter')
if len(guess) == 1 and guess.isalpha() == True:
   print("Good guess!")
else:
   print("Oops! That is not a valid input.")
