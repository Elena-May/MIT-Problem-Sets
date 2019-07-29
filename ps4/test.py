from collections import deque
import string

"""
def load_words(file_name):

    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

WORDLIST_FILENAME = 'words.txt'
valid_words = load_words(WORDLIST_FILENAME)

"""
def build_shift_dict(shift):
        letterstring = string.ascii_lowercase + string.ascii_uppercase
        minusshift = shift - (shift * 2)
        letterstring2 = deque(list(letterstring))
        letterstring2.rotate(minusshift)

        keys = letterstring
        values = letterstring2

        letterdict = dict(zip(keys, values))
        print (letterdict)

        return (letterdict)

letterdict = build_shift_dict(2) 
message_text = 'hello'

"""

for l in message_text:
        for key, value in letterdict.items():
                if key == l:
                        newmessagelist.append(value)

newmessagestring = ''.join(str(c) for c in newmessagelist)

print (newmessagestring)

def apply_shift(letterdict, message_text):
        newmessagelist = []
        for l in message_text:
                        for key, value in letterdict.items():
                                if key == l:
                                        newmessagelist.append(value)

        new_message_shift = ''.join(str(c) for c in newmessagelist)

        return (new_message_shift)


correctw = 0
        
if correctw < len(message_text):
        for number in range (0, 26):
        shift = number 
        shifted_text = apply_shift(shift, message_text)

        for word in shifted_text:
        for vord in valid_words:
                if word == vord:
                correctw += 1

print (shift + ', '  + shifted_text)

"""
message_text = "hello how are you"
message_text_split = message_text.split()
wordstring = ""
newmessagelist = []


print(message_text_split)

for word in message_text_split:
        print ('This is a word ' + word)
        for letter in word:
                for key, value in letterdict.items():
                        if key == letter:
                                wordstring += str(value)
        newmessagelist.append(wordstring)
        wordstring = ''

new_message_shift = ' '.join(str(c) for c in newmessagelist)

print(new_message_shift)