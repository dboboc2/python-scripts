
# the different between , and + for concatenation is when you use
# "+" you must convert the concatenated object to a string

import time #module for sleep
import random #to get random number to pull from txt
from datetime import datetime
		
name = raw_input("Hello, what's your name?\n")
		
print "Hey, " + name + " let's play hangman..."
		
time.sleep(1.2)   
print "Start guessing letters!, enter \"exit\" to exit."
time.sleep(0.5) 

#Now we randomly grab a word from a list of ~5.4k words.
# using a randomly generated number between 1 & 5461
wordList = open('5kwords.txt', 'r')
randNum = int(random.randrange(1, 5461)) # generates random line number

# this loop will read through the list, EX: if randNum is 3, it will read 3 lines.
while(randNum):
	word = wordList.readline()
	randNum -= 1
wordList.close()
word = word[:-1] # THIS REMOVES THE NEWLINE FROM THE STRING

#creates an empty variable to store guesses in.
guesses = ''	
turnCount = 1	# turn starts as one

for char in word: # print out the starting board
	print "_",

while(1):
	while turnCount <= 8:                       
    		guess = raw_input("guess a character: ")
		
		#check if they want to exit
		if(guess == "exit")
			print "Exiting..."
			exit()

		guessLength = len(guess)
		# check if already guessed
		if guess in guesses:
			print "Already guessed", guess + "!"
			continue;

		#check if they are trying to guess the whole word
		if len(word) == guessLength:
			if word == guess:
				print "You won!"
                        	time.sleep(1)
                        	print "let's play again, " + name
                        	break
		else: # if the length is not equal to the word
			if guessLength > 1: # AND the length is greater than 1
				print "Please only enter 1 character OR guess the full word!"
				continue
			guesses += guess  #Concatenate the user's guess to history
  
    		if guess not in word:  
        		turnCount += 1        
        		print "\nWrong"
			#check if out of turns
			if (8 - (turnCount - 1)) == 0 : 
				print "You're out of guesses!"
				print "The word was \"" + word + "\"" 
				break
			elif (8 - (turnCount - 1)) == 1: # grammar :}
				print "You have ", (8 - (turnCount - 1)), " more guess\n" 
 			else:
				print "You have ", (8 - (turnCount - 1)), " more guesses\n"
			
        	# if the turns are equal to zero..
        	if turnCount == 0:
            		print "You Lose"
			time.sleep(1)
			print "let's play again, " + name
		
    		failCount = 0

    		# for every character in word, see if they got all the letters
    		for char in word:
        		if char in guesses:
            			print char,  # comma = space, rather than newline
        		else:
            			print "_",
				failCount += 1
	
    		if failCount == 0:
        		print "You won!"
        		time.sleep(1)
        		print "let's play again, " + name
        		break

	print "How about another word!\n"
	time.sleep(0.5)
	randNum = int(random.randrange(1, 5461)) # generates random line number                                                                                                                   # this loop will read through the list, EX: if randNum is 3, it will read 3 lines
	# but first, reopen the file (resetting the walker)
	wordList = open('5kwords.txt', 'r')
	while(randNum):
		word = wordList.readline()
		randNum -= 1
	wordList.close()
	word = word[:-1] # removes the newline character :)
	turnCount = 1 #reset turn count
	guesses = '' #clear guesses
	for char in word:
		print "_",

  
