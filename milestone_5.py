import random

class Hangman: 
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self,  word_list, num_lives = 5 ):
        self.word = random.choice(word_list) 
        self.word_guessed = list('_'* len(self.word))
        self.num_letters = len(set(self.word)) 
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses =  [] 
        "The mistery word has {num_letters} characters"
        "The mistery word has {word_guessed} characters"
        pass
    
    
    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
            
        '''
        if letter.lower()  in self.word:
            print(f"Good guess! {letter} is in the word.")
            for i, letters in  enumerate(self.word):
                if self.word[i] == letter:
                   self.word_guessed[i] = letters
                   print(self.word_guessed)
                   pass
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            pass
        
    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
           letter = input('Enter a letter') 
           if len(letter) != 1 or letter.isalpha() == False:
            print(f"Invalid letter. Please, enter a single alphabetical character.")
           elif letter in self.list_of_guesses:
            print("You already tried that letter!")
           else:
            self.check_letter(letter) 
            
           
           self.list_of_guesses.append(letter)
           break
           
           
           
def play_game(word_list):
    
    game = Hangman(word_list, num_lives=5) 
    while True:
        if game.num_lives == 0: 
            print('You lost!')
            break
        if game.num_letters >= 0:
            game.ask_letter() 
        if  game.num_lives != 0 and  game.num_letters  <= 0: 
            print('Congratulations. You won the game!')
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)


    

            