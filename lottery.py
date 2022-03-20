#Stupid simple lottery simulator by Gwen Virtue
#Make an array of ten integers between 1 and 10, then select four of those integers at random and display as winning ticket.
#Will make use of this in a different script

from random import choice
from random import randint

lottery = []
winner = []

for i in range(10):
	lottery.append(randint(1,10))

for i in range(4):
	winner.append(choice(lottery))

print("You are a winner if your ticket matches these numbers:", end = " ")
print(*winner, sep = " | ")

