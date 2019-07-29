import math
import random
import string

"""
WORDLIST_FILENAME = "words.txt"

def load_words():

    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.

    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist
"""
"""
hand = {'h': 1, 'a': 1, 't': 1, 'b': 1, 'j': 2}
word = 'beg' 
new_hand = {}
value = 0 


for key in hand:
    for l in word: 
        if key != l: 
            print (key)
            if l not in new_hand:
                new_hand[l] = 1
                #print (new_hand)
            else:
                new_hand[l] = new_hand[l] + 1
                #print (new_hand)

        elif key == l:
            pass 

print (new_hand)

for key, value in hand.items():
    if key not in word:
        new_hand[key] = value
        
    elif key in word:
        pass

print (new_hand)

result = True

for l in word:
    if l in hand.keys():
        if hand[l] <= 0:
            result = False
        elif hand[l] > 0:
            hand[l] -= 1

    if l not in hand.keys():
        result = False
    
print(result)

"""

VOWELS = 'aeiou*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
VOWELS1 = 'aeiou'

"""
n = HAND_SIZE
hand={}
num_vowels = int(math.ceil(n / 3))

for i in range(num_vowels):
    if '*' in hand.keys():
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    if '*' not in hand.keys():
        hand['*'] = hand.get('*', 0) + 1

for i in range(num_vowels, n):    
    x = random.choice(CONSONANTS)
    hand[x] = hand.get(x, 0) + 1

print (hand)


test = {'a': 2, 'b': 3, 'c': 1}

letter = 'a'

if letter in test.keys():
    newletter = random.choice(VOWELS)
    test[newletter] = test[letter]

del test[letter]

print (test)
"""
word = 'c*t'
hand = {'c': 1, 'a': 1, 't': 1, '*': 1}
word_list = ['cat', 'egg', 'lemon']
result = True
listvowels = list(VOWELS1)
listword = list(word)

"""
# come back to this and make it simpler, less nested loops
if '*' in word:
    #enumerate, built-in python function, automatic counter for a list
    # index = offset, place in the list 
    for windex, w in enumerate(word_list):
        listword = list(w)
        for v in listvowels:
            for index, i in enumerate(listword):
                if v == i:
                    print (i)
                    listword[index] = '*'
        #put listword back into wordlist 
        word_list[windex] = "".join(listword)
    
    if word not in word_list:
        print(word_list)
        result = False
else:
    if word not in word_list:
        result = False

"""
if word not in word_list:
    if '*' not in word:
        result = False
    elif '*' in word:
            for w in listword:
                for v in listvowels:
                    w.replace('*', v, 1)
                    print (listword)
                    if word not in word_list:
                        result = False
                    else:
                        result = True 

for l in word:
    if l in hand.keys():
        # doesn't know what value is 
        if hand[l] <= 0:
            result = False
        elif hand[l] > 0:
            hand[l] -= 1

if l not in hand.keys():
    result = False

print (result)
