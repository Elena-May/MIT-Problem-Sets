import unittest
import ps3 

class ps3testing (unittest.TestCase):
    def setUp(self):
        print ("Operations to run before a test")
    
    def tearDown(self):
        print("operations to run before a test")

    def test_get_word_score(self):
        word = "horse"
        SLV = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
        n = 7
        result = ps3.get_word_score(word, n)
        print("\t testing get_word_score ")
        #its not 8 
        self.assertEqual(result, 37)

    def test_update_hand(self):
        hand = {'h': 1, 'a': 1, 't': 1, 'b': 1, 'j': 2}
        word = 'hat' 
        result = ps3.update_hand(hand, word)
        print ("t\ Testing show_possible matches ")
        self.assertEqual(result, {'b': 1, 'j': 2})

    def test_is_valid_word(self):
        word = 'c*t'
        hand = {'c': 1, 'a': 1, 't': 1, '*': 1}
        word_list = ('cat', 'egg', 'lemon')
        result = ps3.is_valid_word(word, hand, word_list)
        print ("t\ Testing is_valid_word")
        self.assertEqual(result, True)





if __name__ == '__main__':
    unittest.main() #invokes a runner on the extended class 