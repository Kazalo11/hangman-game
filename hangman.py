import random


stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
def guessing(word):
	guess2 = list(word)
	start = ["_"]*len(word)
	print("Start of game")
	print(stages[-1])
	print(' '.join(start))
	errors = set()
	while len(errors) < 6:
		attempt = input("Guess a letter: ")
		if attempt not in guess2:
			print("This letter is not in the word")
			errors.add(attempt)
		else:	
			for i in range(len(guess2)):
				if guess2[i] == attempt:
					start[i] = attempt
		print(' '.join(start))
		if ''.join(start) == guess:
			print("You guessed the word")
			break
		print(stages[6-len(errors)])
		print(f"You have made {len(errors)} errors")
		print(f"The wrong letters are: {' '.join(errors)} ")
		print(f"You have {6-len(errors)} wrong attempts left")
	if len(errors) >= 6:
		print("You have made too many errors")
		print(f"The correct word was {word} ")



options = input("Do you want to suggest a word (Y) or choose a random word (N) (Y/N)? ")

if options == "Y":
	
	guess = input("Enter a word: ")
	guessing(guess)

if options == "N":
	with open ('words.txt') as f:
		lines = f.read().splitlines()
	line = random.choice(lines)
	guess = ''.join(line)
	
	guessing(guess)