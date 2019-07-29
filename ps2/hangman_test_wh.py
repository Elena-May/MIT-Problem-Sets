import unittest
import hangman as hngmn 

class hangmantestswh(unittest.testcase):
    def setUp(self):
        print ("Operations to run before a test")
    
    def tearDown(self):
        print("operations to run before a test")
    
    def test_match_with_gaps(self):
        word_so_far = 't_ a_ n_ r'
        other_word = 'trainer'
        result = hngmn.match_with_gaps(word_so_far, other_word)
        print("\t Testing is_word_guessed")
        self.assertEqual(result, True)
    

    def test_show_possible_matches(self):
        wordlist = ['hat', 'cat', 'rat', 'sat', 'bacon']
        myword = '__t'
        result = hngmn.show_possible_matches(my_word)
        print("\t Testing is_word_guessed")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main() #invokes a runner on the extended class 
