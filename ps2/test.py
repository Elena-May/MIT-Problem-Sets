def match_with_gaps(my_word, other_word):
    my_word2 = my_word.replace("_ ", "")
    my_word3 = my_word.replace(" ", "")
    
    #need to add the part about .count
    if len(my_word3) == len(other_word) and set(my_word2).issubset(other_word):
        return True
    else:
        return False

wordlist = ['hat', 'cat', 'rat', 'sat', 'bacon']
my_word = '_ _ t'
possible_words = []

for other_word in wordlist:
    #print (other_word) 
    if match_with_gaps(my_word, other_word) == True: 
        possible_words.append(other_word)
      
print(possible_words)