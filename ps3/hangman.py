
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
	return random.choice(wordlist)
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
	checker = 0
	for y in range(len(secret_word)):
		for x in letters_guessed: 
			if secret_word[y] == x:
				checker = 1
			else: 
				checker = 0
			if checker == 1:
				break
		if checker == 0:
			return False
		else: 
			checker = 0
	return True
		
			
	
			


def get_guessed_word(secret_word, letters_guessed):
	guessedwordarr = []
	guessedword = ''
	checker = 0
	for y in range(len(secret_word)): 
		for x in letters_guessed:
			if secret_word[y] == x:
				guessedwordarr.append(f" {x}")
				checker = 1
			else:
				checker = 0
			if checker == 1: 
				break
		if checker == 0: 
			guessedwordarr.append(" _")
	for letter in guessedwordarr: 
		guessedword += letter
	return guessedword
		
				


def get_available_letters(letters_guessed):
	arrofletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	availableletters = ''
	for x in range(len(arrofletters) - len(letters_guessed)):
		for letter in letters_guessed:
			if arrofletters[x] == letter: 
				arrofletters.remove(letter)
			else:
				pass
	for letter in arrofletters:
		availableletters += letter
	return availableletters

def is_warning(letters_guessed, userguess):
	if len(letters_guessed) == 0:
		return False
	else:
		for x in range(len(letters_guessed)):
			if letters_guessed[x] == userguess:
				return True
		return False
				
def uniqueletters(secret_word):
	arrofletters = []
	for x in range(len(secret_word)):
		arrofletters.append(secret_word[x])
	arrofletters = set(arrofletters)
	return(len(arrofletters))
	
def uniquelettersarr(secret_word):
	arrofletters = []
	for x in range(len(secret_word)):
		arrofletters.append(secret_word[x])
	arrofletters = set(arrofletters)
	return(arrofletters)

def hangman(secret_word):
	print(secret_word)
	print("Welcome to the game Hangman!")
	print(f"I am thinking of a word that is {len(secret_word)} letters long.")
	print("---------------------")
	guessesleft = 6
	warningsleft = 3
	correct_letters_guessed = []
	letters_guessed = []
	userguess = ''
	while guessesleft != 0:
		print(f"You have {guessesleft} guesses left.")
		print("Available Letters:", get_available_letters(letters_guessed))
		userguess = input("Please guess a letter:")
		print(is_warning(letters_guessed, userguess))
		if (is_warning(letters_guessed, userguess)) == False:
			letters_guessed.append(userguess)
			for x in range(len(secret_word)):
				checker = 0
				if userguess == secret_word[x]:
					correct_letters_guessed.append(userguess)
					print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
					checker = 1
					break
			if checker == 0:
				print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
				guessesleft -= 1
				break
		else:
			warningsleft -= 1
			print(f"Oops! You've already guessed that letter. You now have {warningsleft} warnings")
		if is_word_guessed(secret_word, letters_guessed) == True: 
			print("Congradulations, you won!")
			totalpoints = uniqueletters(secret_word) * guessesleft
			print("Total Points:", totalpoints)
			break
		if guessesleft == 0 or warningsleft == 0:
			print("Sorry, you have run out of guesses")
			print(f'The secret word was "{secret_word}"')

		

def match_with_gaps(my_word, other_word):
	stripped_word = my_word.replace(" ", "")
	if len(stripped_word) == len(other_word):
		for x in range(len(stripped_word)):
			if stripped_word[x] == other_word[x]: 
				pass
			elif stripped_word[x] != other_word[x] and stripped_word[x] != '_': 
				return False
	else: 
		return False
	return True



def show_possible_matches(my_word):
	arrofwords = []
	stripped_word = my_word.replace(" ", "")
	possible_matches = []
	print(stripped_word)
	with open(WORDLIST_FILENAME, 'r') as file:
		for line in file:
			for word in line.split():
				checker = 1
				if len(word) == len(stripped_word):
					usedletters = []
					for x in range(len(stripped_word)):
						if stripped_word[x] == word[x]:
							pass
						elif stripped_word[x] != word[x] and stripped_word[x] != '_':
							checker = 0
						else:
							for letter in usedletters:
								if letter == word[x]:
									checker = 0
				else: 
					checker = 0
				if checker == 1: 
					possible_matches.append(word)
				else:
					pass
	return possible_matches	

							
					
		



def hangman_with_hints(secret_word):
	print("Welcome to the game Hangman!")
	print(f"I am thinking of a word that is {len(secret_word)} letters long.")
	print("---------------------")
	guessesleft = 6
	warningsleft = 3
	correct_letters_guessed = []
	letters_guessed = []
	userguess = ''
	while guessesleft != 0:
		print(f"You have {guessesleft} guesses left.")
		print("Available Letters:", get_available_letters(letters_guessed))
		userguess = input("Please guess a letter:")
		if (is_warning(letters_guessed, userguess)) == False:
			letters_guessed.append(userguess)
			for x in range(len(secret_word)):
				checker = 0
				if userguess == secret_word[x]:
					correct_letters_guessed.append(userguess)
					print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
					checker = 1
					break
			if checker == 0:
				print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
				guessesleft -= 1
		else:
			warningsleft -= 1
			print(f"Oops! You've already guessed that letter. You now have {warningsleft} warnings")
		if is_word_guessed(secret_word, letters_guessed) == True: 
			print("Congradulations, you won!")
			totalpoints = uniqueletters(secret_word) * guessesleft
			print("Total Points:", totalpoints)
			break
		if guessesleft == 0 or warningsleft == 0:
			print("Sorry, you have run out of guesses")
			print(f'The secret word was "{secret_word}"')
		if guessesleft <= 3:
			print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))



if __name__ == "__main__":
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word) 
