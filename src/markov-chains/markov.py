from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    contents = open(file_path).read()
    #open file and return a string including spaces

    # print type(contents)

    return contents
    """This should be a variable that contains your file text as one long string"""

#contents = open_and_read_file("green-eggs.txt")
#Rebind contents to global scope since the next function will call it.


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """


    # your code goes here

    chains = {}
    #create empty dictionary to contain all key pair values
  

    words = text_string.split() # splitting contents to words list by empty spaces

    indices = range((len(words)) - 2) 
    # indices is a list of integers that represent the index position of each word in the words list 
    #we subtract 2 from the entire range because the value_for_key = words[i+2]

    for i in indices:
        #for each i in indices, the for loop below will bind the index position of each word with each i.
        # for word in words:
        key_tuple = ((words[i]),(words[i+1]))
        # print key_tuple
        value_for_key = [words[i+2]]
        # print value_for_key
        # chains[key_tuple] = value_for_key 
        # print chains
        #for each word in words list, the first two words are rebounded to tup to create a key. The key is paired with the value.


        chains[key_tuple] = chains.get(key_tuple,[]) + value_for_key

    print chains
    return chains
    

# print make_chains(contents)

    



    

    

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
