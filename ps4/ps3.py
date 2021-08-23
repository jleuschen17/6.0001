import math
import random
import string
import re

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALLLETERS = 'abcdefghijklmnopqrstuvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0,
}

WORDLIST_FILENAME = "words.txt"

def load_words():
	print("Loading word list from file...")
	inFile = open(WORDLIST_FILENAME, 'r')
	wordlist = []
	for line in inFile:
		wordlist.append(line.strip().lower())
	print("  ", len(wordlist), "words loaded.")
	return wordlist
def get_frequency_dict(sequence):
	freq = {}
	for x in sequence:
		freq[x] = freq.get(x,0) + 1
	return freq

def get_word_score(word, n):
	word_points = 0
	word = word.lower()
	word_length = len(word)
	wordarr = list(word)
	comp1 = 0
	for letter in wordarr:
		comp1 += SCRABBLE_LETTER_VALUES[letter]
	comp2 = ((7 * word_length) - (3 * (n - word_length)))
	if comp2 > 1:
		pass
	else:
		comp2 = 1
	return(comp1 * comp2)

def display_hand(hand):
	for letter in hand.keys():
		for j in range(hand[letter]):
			print(letter, end=' ')
	print()

def deal_hand(n):
	hand={}
	num_vowels = int(math.ceil(n / 3)) - 1
	for i in range(num_vowels):
		x = random.choice(VOWELS)
		hand[x] = hand.get(x, 0) + 1

	for i in range(num_vowels + 1, n):    
		x = random.choice(CONSONANTS)
		hand[x] = hand.get(x, 0) + 1
	hand['*'] = 1
	return hand

def update_hand(hand, word):
	word = word.lower()
	wordarr = list(word)
	newhand ={}
	for key in hand:
		newhand[key] = hand[key]
	for letter in wordarr:
		if newhand[letter] > 1:
			newhand[letter] = newhand[letter] - 1
		else:
			newhand.pop(letter)
	return(newhand)

def isvowel(letter):
	if letter == 'a':
		return True
	elif letter == 'e':
		return True
	elif letter == 'i':
		return True
	elif letter == 'o':
		return True
	elif letter == 'u':
		return True
	else:
		return False

def is_valid_word(word, hand, word_list):
	word = word.lower()
	wordarr = list(word)
	handcopy = {}
	for key in hand:
		handcopy[key] = hand[key]
	for letter in wordarr:
		checker = 0
		for key in handcopy:
			if letter == key:
				if handcopy[key] < 1:
					return False
				elif key == letter:
					handcopy[key] = handcopy[key] - 1
					checker = 1
		if checker == 0:
			return False
	word = word.replace("*", ".")
	vowelarr = list(VOWELS)
	def searchinitial(word, wordlist):
		for x in word_list:
			if re.search(word, x):
				return(word)
				break
	for vowel in vowelarr:
		novelword = str(searchinitial(word, word_list)).replace('.', vowel)
		for word2 in word_list:
			if novelword == word2:
				return True
	return False

def calculate_handlen(hand):
	len = 0
	for key in hand: 
		len += hand[key]
	return(len)

def play_hand(hand, word_list):
	totalpoints = 0
	word = ''
	while word != '!!':
		print('Current Hand: ', end = '')
		display_hand(hand)
		word = input('Enter word or "!!" to indicatethat you are finished: ')
		if is_valid_word(word, hand, word_list) == True:
			print(f'"{word}" earned ',get_word_score(word, calculate_handlen(hand)),' points\n')
			totalpoints += get_word_score(word, calculate_handlen(hand))
			hand = update_hand(hand, word)
		elif word != '!!':
			print('Dumbass! That is not a valid word. Please choose another word.\n')
		if calculate_handlen(hand) == 0:
			print(f'\nYou ran out of letters. Total Score: {totalpoints} points')
			break
		elif word == '!!':
			print(f'\nTotal score: {totalpoints} points')
	return totalpoints

def substitute_hand(hand, letter):
	randletter = str(random.choice(ALLLETERS))
	newhand = {}
	for key in hand:
		while randletter == key: 
			randletter = str(random.choice(ALLLETERS))
		newhand[key] = hand[key]
	for key in newhand:
		if key == letter:
			del newhand[key]
			newhand[randletter] = hand[key]
	return(newhand) 

def play_game(word_list):
	numofhands = 1
	cumulatedpoints = 0
	hand = deal_hand(HAND_SIZE)
	numofhands = int(input("Enter total number of hands: "))
	while numofhands > 0:
		print('Current Hand: ', end = '')
		display_hand(hand)
		usersubresponse = input("Would you like to subisitute a letter? ")
		usersubresponse.lower()
		if usersubresponse == 'yes':
			letter = input('Which letter would you like to replace: ')
			hand = substitute_hand(hand, letter)
		else: 
			pass
		cumulatedpoints += play_hand(hand, word_list)
		numofhands -= 1
		if numofhands == 0:
			break
		userhandchoice = input('Would you like to replay the hand: ')
		userhandchoice = userhandchoice.lower()
		if userhandchoice == 'yes': 
			pass
		else: 
			hand = deal_hand(HAND_SIZE)
	print('\nTotal score over all hands:', cumulatedpoints)
	
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
