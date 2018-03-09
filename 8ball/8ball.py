# a simple 8-ball script, by Daniel Boboc, 2/21/18
import random
import time
import os
from datetime import datetime
def main():
	while(1):
		os.system("clear")
		random.seed(datetime.now())
		choice = name = raw_input("What is your Question?\n")
		for x in range(0,13):
			time.sleep(0.15)
			print '.' *  int(random.randrange(3,13))
		
		answer = random.randrange(1,20)
		switch_demo(answer)
		for x in xrange(3, 0, -1):
			print('.' * x)
		time.sleep(3)



#uses a parameter, argument to decide what to print, printing "invalid random num" as DEFAULT
def switch_demo(argument):
    switcher = {
        1: "It is certain",
        2: "It is decidedly so",
        3: "Without a doubt",
        4: "Yes, definitely",
        5: "You may rely on it",
        6: "As I see it, yes",
        7: "Most likely",
        8: "Outlook good",
        9: "Yes.",
        10: "Signs point to yes",
        11: "Yes.",
        12: "Ask again later",
	13: "No.",
	14: "Cannot predict now",
        15: "Concentrate and ask again",
        16: "Don't count on it",
        17: "My reply is no",
        18: "My sources say no",
        19: "Outlook not so good",
        20: "Very doubtful",
    }
    print switcher.get(argument, "Invalid random num\n")



if __name__ == "__main__":
	main()













