# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import random 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.

    base case = if the sequence is a single character
    '''
    # if sequence is a single character 
    if len(sequence) == 1:
        # return list containing 'sequence'
        sequence_result = list(sequence)
        return sequence_result
    # creating a method that gives a sequence of all permutations except the first character (recursion)
    #else:
    
    permutations = []
    
    #make a permutation loop 
    #starting to work... don't understand how 

    # for a sequence of everything but the first character 
    # why does it print c and not b to start with
    for p in get_permutations(sequence[1:]):
        print ('This is p:',p)
        # adds an empty space to p (+1)
        # starting with the first character in the sequence 
        for i in range(len(p) + 1):
            # everything before and not including i + the first character in the sequence + everything after and including i 
            permutations.append(p[:i] + sequence[:1] + p[i:])
    return permutations

    # [:i] - means end the sequence with i 

    # need it to unbuild the sequence till it gets to one and then keep adding them back in again
    # so remove the first character, 


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 

    pass #delete this line and replace with your code here
