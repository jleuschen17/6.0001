# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
class Message(object):
    def __init__(self, text):
    	self.message_text = text
    	self.valid_words = load_words(WORDLIST_FILENAME)
        #'''
        #Initializes a Message object
                
        #text (string): the message's text

        #a Message object has two attributes:
            #self.message_text (string, determined by input text)
            #self.valid_words (list, determined using helper function load_words)
        #'''
        #pass #delete this line and replace with your code here

    def get_message_text(self):
    	return self.message_text
        #'''
        #Used to safely access self.message_text outside of the class
        
        #Returns: self.message_text
        #'''
        #pass #delete this line and replace with your code 

    def get_valid_words(self):
        copyofwords = self.valid_words
        return copyofwords

    def build_shift_dict(self, shift):
    	loweralphabet = 'abcdefghijklmnopqrstuvwxyz'
    	upperalphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    	shiftdict = {}
    	lowerlist = list(loweralphabet)
    	upperlist = list(upperalphabet)
    	for x in range(len(lowerlist)):
    		if x + shift > 25:
    			shiftdict[lowerlist[x]] = lowerlist[x + shift - 26]
    		else:
    			shiftdict[lowerlist[x]] = lowerlist[x + shift]
    	for x in range(len(upperlist)):
    		if x + shift > 25:
    			shiftdict[upperlist[x]] = upperlist[x + shift - 26]
    		else:
    			shiftdict[upperlist[x]] = upperlist[x + shift]
    	return shiftdict
    def apply_shift(self, shift):
    	textlist = list(self.message_text)
    	shiftedword = ''
    	shifteddict = self.build_shift_dict(shift)
    	for letter in textlist:
    		if letter == ' ':
    			shiftedword += ' '
    		elif letter == '.' or letter == '!' or letter == '?' or letter == ',' or letter == ':' or letter == ';' or letter == '\n':
    			newletter = letter
    			shiftedword += newletter
    		else:
	    		newletter = shifteddict[letter]
	    		shiftedword += newletter
    	return shiftedword
        #'''
        #Applies the Caesar Cipher to self.message_text with the input shift.
        #Creates a new string that is self.message_text shifted down the
        #alphabet by some number of characters determined by the input shift        
        
        #shift (integer): the shift with which to encrypt the message.
        #0 <= shift < 26

        #Returns: the message text (string) in which every character is shifted
             #down the alphabet by the input shift
        #'''

class PlaintextMessage(Message):
    def __init__(self, text, shift):
    	self.message_text = text
    	self.valid_words = load_words(WORDLIST_FILENAME)
    	self.shift = shift
    	self.encryption_dict = self.build_shift_dict(shift)
    	self.message_text_encrypted = self.apply_shift(shift)
    	self.Message = Message(text)
        #'''
        #Initializes a PlaintextMessage object        
        
        #text (string): the message's text
        #shift (integer): the shift associated with this message

        #A PlaintextMessage object inherits from Message and has five attributes:
            #self.message_text (string, determined by input text)
            #self.valid_words (list, determined using helper function load_words)
            #self.shift (integer, determined by input shift)
            #self.encryption_dict (dictionary, built using shift)
            #self.message_text_encrypted (string, created using shift)

        #'''
        #pass #delete this line and replace with your code here

    def get_shift(self):
    	return self.shift
        #'''
        #Used to safely access self.shift outside of the class
        
        #Returns: self.shift
        #'''
        #pass #delete this line and replace with your code here

    def get_encryption_dict(self):
    	encryption_dict_copy = self.encryption_dict
    	return encryption_dict_copy
        #'''
        #Used to safely access a copy self.encryption_dict outside of the class
        
        #Returns: a COPY of self.encryption_dict
        #'''
        #pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
    	return self.message_text_encrypted
        #'''
        #Used to safely access self.message_text_encrypted outside of the class
        
        #Returns: self.message_text_encrypted
        #'''
        #pass #delete this line and replace with your code here

    def change_shift(self, shift):
    	self.shift = shift
    	self.get_encryption_dict()
    	self.get_message_text_encrypted()
        #'''
        #Changes self.shift of the PlaintextMessage and updates other 
        #attributes determined by shift.        
        
        #shift (integer): the new shift that should be associated with this message.
        #0 <= shift < 26

        #Returns: nothing
        #'''
        #pass #delete this line and replace with your code here

class CiphertextMessage(Message):
    def __init__(self, text):
    	self.message_text = text
    	self.valid_words = load_words(WORDLIST_FILENAME) 
    	self.Message = Message(text)
    	
        #'''
        #Initializes a CiphertextMessage object
                
        #text (string): the message's text

        #a CiphertextMessage object has two attributes:
            #self.message_text (string, determined by input text)
            #self.valid_words (list, determined using helper function load_words)
        #'''
        #pass #delete this line and replace with your code here

    def decrypt_message(self):
    	finalshift = 0
    	maxnumofwords = 0
    	message_text_copy = ''
    	finalmessage = ''
    	for x in range(26):
    		message_text_copy = self.message_text
    		numofwords = 0
    		shift = x
    		message_text_copy = self.apply_shift(shift)
    		messagelist = message_text_copy.split()
    		for messageword in messagelist:
    			if is_word(self.valid_words, messageword) == True:
    				numofwords += 1
    		if numofwords > maxnumofwords:
    			maxnumofwords = numofwords
    			finalshift = x
    			finalmessage = message_text_copy
    	return finalshift, finalmessage
    			
    			
        #'''
        #Decrypt self.message_text by trying every possible shift value
        #and find the "best" one. We will define "best" as the shift that
        #creates the maximum number of real words when we use apply_shift(shift)
        #on the message text. If s is the original shift value used to encrypt
        #the message, then we would expect 26 - s to be the best shift value 
        #for decrypting it.

        #Note: if multiple shifts are equally good such that they all create 
        #the maximum number of valid words, you may choose any of those shifts 
        #(and their corresponding decrypted messages) to return

        #Returns: a tuple of the best shift value used to decrypt the message
        #and the decrypted message text using that shift value
        #'''
        #pass #delete this line and replace with your code here
if __name__ == '__main__':
	inFile = open("story.txt", "r")
	messageI = PlaintextMessage(inFile.read(), 5)
	encryptedsentance = messageI.get_message_text_encrypted()
	print('Encrypted Sentance: ',encryptedsentance)
	decryptI = CiphertextMessage(encryptedsentance)
	decryptedsentance = decryptI.decrypt_message()[1]
	print('Decrypted Sentance: ',decryptedsentance)
	numberofshifts = decryptI.decrypt_message()[0]
	print('Number of shifts to decrypt: ',numberofshifts)

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    #pass #delete this line and replace with your code here
