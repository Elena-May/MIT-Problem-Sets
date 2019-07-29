# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_list = list(secret_word)

    #says whether one list is the subset of another, unsequenced and without repeats  
    result = set(secret_word_list).issubset(letters_guessed)
    return result 


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.

    (_ ) unknown letters
    if secret_word isnt in letters_guessed
    replace letter in secret_word with (_ )
    print secret_word
    '''
    word_so_far_list = list()
    for letter in secret_word:
      if letter in letters_guessed:
        #standard practice to use +=
        word_so_far_list.append(letter)

      elif letter not in letters_guessed:
        letter = "_ "
        word_so_far_list.append(letter)
    #makes word_so_far list into a string
    word_so_far = ''.join(word_so_far_list)
    return word_so_far
      
# think this has issues 
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters_list = list()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
      if letter not in letters_guessed:
        available_letters_list.append(letter)

    available_letters = ''.join(available_letters_list)
    return available_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3 
    print ('You have' + str(warnings) + ' warnings left')

    guesses = 0

    secret_word_length = len(secret_word)

    print ('I am thinking of a word that is ' + str(secret_word_length) + ' letters long')
    print ('You have ' + str(secret_word_length + 4) + ' guesses left')
    
    letters_guessed = list()

    my_word = get_guessed_word(secret_word, letters_guessed) 

    #while not would be prettier
    while my_word != secret_word and guesses < (secret_word_length + 4) and warnings != 0: 
      guesses += 1 
      guessed_letter = (input('Guess a letter: '))
  
      if guessed_letter.isdigit() == True or guessed_letter in letters_guessed:
        warnings = warnings - 1

        if warnings == 0:
          print ('You ran out of warnings! The word was ' + secret_word)
        
        else:
          print ('You have ' + str(warnings) + ' warnings left')
          print ('--------------')
  
      elif guessed_letter.isdigit() == False and guessed_letter not in letters_guessed:  
        letters_guessed.append(guessed_letter)
        
        print ('Available letters: ' + get_available_letters(letters_guessed))
        print ('This is your word so far: ' + get_guessed_word(secret_word, letters_guessed))
        print ('You have ' + str((secret_word_length + 4) - guesses) + ' guesses left')
        print ('--------------')

        if guesses >= (secret_word_length + 4):
          print ('You lose! The word was ' + secret_word)
    
        elif my_word == True:
          print ('Well done! The word was ' + secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    
    strip of all the gaps in the words
    check the length
    iterate through the words
    go through an count the number of letters 

    or just use set. issubset again

    ''' 
    my_word2 = my_word.replace("_ ", "")
    my_word3 = my_word.replace(" ", "")

    if len(my_word3) == len(other_word) and set(my_word2).issubset(other_word):
      return True
    else:
      return False




def show_possible_matches(my_word, wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''   
    possible_words = []
  
    for other_word in wordlist:
      if match_with_gaps(my_word, other_word) == True: 
        possible_words.append(other_word)
      
    return possible_words
      



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    warnings = 3 
    print ('You have' + str(warnings) + ' warnings left')

    guesses = 0

    secret_word_length = len(secret_word)

    print ('I am thinking of a word that is ' + str(secret_word_length) + ' letters long')
    print ('You have ' + str(secret_word_length + 4) + ' guesses left')
    
    letters_guessed = list()
    
    my_word = get_guessed_word(secret_word, letters_guessed)
    
    #while not would be prettier
    while my_word != secret_word and guesses < (secret_word_length + 4) and warnings != 0: 
      guesses += 1 
      guessed_letter = (input('Guess a letter: ')) 
  
      if guessed_letter.isdigit() == True or guessed_letter in letters_guessed:
        warnings = warnings - 1

        if warnings == 0:
          print ('You ran out of warnings! The word was ' + secret_word)
        
        else:
          print ('You have ' + str(warnings) + ' warnings left')
          print ('--------------')
      
      elif guessed_letter == "*": 
        possible_matches = show_possible_matches(my_word, wordlist)
        print ('Available letters: ' + get_available_letters(letters_guessed))
        print ('This is your word so far: ', my_word)
        print ('These are the possible words that secret_word could be:', possible_matches)
        print ('--------------')
  
      elif guessed_letter.isdigit() == False and guessed_letter not in letters_guessed:  
        letters_guessed.append(guessed_letter)
        my_word = get_guessed_word(secret_word, letters_guessed)
        
        print ('Available letters: ' + get_available_letters(letters_guessed))
        print ('This is your word so far: ' + my_word)
        print ('You have ' + str((secret_word_length + 4) - guesses) + ' guesses left')
        print ('--------------')

        if guesses >= (secret_word_length + 4):
          print ('You lose! The word was ' + secret_word)
    
        elif my_word == True:
          print ('Well done! The word was ' + secret_word)
      
      



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

"""
when python starts the program it sets the __name__ to __main__ 
So it runs these first?
"""

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
