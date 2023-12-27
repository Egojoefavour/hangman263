word_list = ['apple', 'banana', 'orange', 'grape', 'cherry']
print(word_list)

import random

print(random.choice(word_list))

word = []
for fruit in word_list:
 
  if random.choice(word_list) == fruit:
   word.append(fruit)
print(word)

guess = input('Enter a letter')
for char in guess:
 if len(guess) == 1 and char.isalpha() == True:
   print("Good guess!")
   
 else:
  print("Oops! That is not a valid input.")
