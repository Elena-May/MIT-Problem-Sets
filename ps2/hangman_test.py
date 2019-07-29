import unittest
import hangman as hngmn

"""
class hangmantests(unittest.TestCase):
    def setUp(self):
        print ("Operations to run before a test")
    
    def tearDown(self):
        print("operations to run before a test")
    
    def test_is_word_guessed(self):
        secret_word = 'hat'
        letters_guessed = ['a', 'b', 'c']
        result = hngmn.is_word_guessed(secret_word, letters_guessed)
        print("\t Testing is_word_guessed")
        self.assertEqual(result, False)
    
    def test_get_guessed_word(self):
        secret_word = 'hat'
        letters_guessed = ['a', 'b', 'c']
        result = hngmn.get_guessed_word(secret_word, letters_guessed)
        print("\t Testing get_guessed_word")
        self.assertEqual(result, '_ a_ ')

    def test_get_available_letters(self):
        letters_guessed = ['a', 'b', 'c']
        result = hngmn.get_available_letters(letters_guessed)
        print("\t Testing get_available_letters")
        self.assertEqual(result, 'defghijklmnopqrstuvwxyz') 
"""

class hangmantestswh(unittest.TestCase):
    def setUp(self):
        print ("Operations to run before a test")
    
    def tearDown(self):
        print("operations to run before a test")
    
    def test_match_with_gaps(self):
        my_word = 't_ a_ n_ r'
        other_word = 'trainer'
        result = hngmn.match_with_gaps(my_word, other_word)
        print("\t Testing match_with_gaps ")
        self.assertEqual(result, True)
    
    def test_show_possible_matches(self):
        wordlist = ['hat', 'cat', 'rat', 'sat', 'bacon']
        my_word = '_ _ t'
        result = hngmn.show_possible_matches(my_word, wordlist)
        print (result, type(result))
        print("\t Testing show_possible_matches ")
        self.assertEqual(result, ['hat', 'cat', 'rat', 'sat'])

    def test_update_hand(self):
        hand = {h:1, a:1, t: 1, b: 1, j: 2}
        word = hat 
        result = ps3.update_hand(hand, word)
        print ("t\ Testing show_possible matches ")
        self.assertEqual(result, {b: 1, j: 2})

if __name__ == '__main__':
    unittest.main() #invokes a runner on the extended class 


