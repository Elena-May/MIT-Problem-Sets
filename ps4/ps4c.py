# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import random

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

def get_permutations(sequence):
    
    if len(sequence) == 1:
        sequence_result = list(sequence)
        return sequence_result
    
    permutations = []
    for p in get_permutations(sequence[1:]):
        for i in range(len(p) + 1):
            permutations.append(p[:i] + sequence[:1] + p[i:])
        
    return permutations

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.get_valid_words()
    
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        self.vowels_perm_dict = dict(zip(VOWELS_LOWER, vowels_permutation))

        return self.vowels_perm_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        message_text_split = self.message_text.split()
        newmessagelist = []
        letters = []
        wordstring = ""

        for word in message_text_split:
            for letter in word:
                for key, value in transpose_dict.items():
                    if letter != key:
                        letters += str(letter)
                    elif letter == key:
                        letters += str(value)

                if(len(set(letters))==1):
                    letter = letters[0]
                else:
                    for l in letters:
                        if letters.count(l) == 1:
                            letter = l
                        else:
                            letter = letter
                letters = []
                wordstring += letter
            newmessagelist.append(wordstring)
            wordstring = ""

        new_message_shift = ' '.join(str(c) for c in newmessagelist)
        return new_message_shift

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        self.all_perms = get_permutations(VOWELS_LOWER)
        
        dict_list = []
        transposed_message_list = []
        tml_correct = []

        for perm in self.all_perms:
            voweldict = SubMessage.build_transpose_dict(self, perm)
            dict_list.append(voweldict)

        for lis in dict_list: 
            transpose_message = SubMessage.apply_transpose(self, lis)
            transposed_message_list.append(transpose_message)

        for message in transposed_message_list:
            lis0 = message.lower()
            lis1 = lis0.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
            lis2 = lis1.split()
            tml_correct.append(lis2)
        
        word_count = 0
        correct_word_count = 0
        shifted_text_correct = 0
        
        for text in tml_correct:
            for word in self.valid_words:
                for m_word in text:
                    if m_word == word:
                        word_count += 1
                        print(word_count)
            
            if word_count > correct_word_count:
                correct_word_count = word_count 
                shifted_text_correct = text

            word_count = 0 
        
        return shifted_text_correct



if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello, this better work")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message: ", message.get_message_text(), "Permutation: ", permutation)
    print("Expected encryption: ", "Hallu  Wurld!")
    print("Actual encryption: ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())