#Stupid simple lottery simulator by Gwen Virtue
#Make an array of ten integers between 1 and 10, then select four of those integers at random and display as winning ticket.
#Will make use of this in a different script

from random import choice
from random import randint

class Lottery:

	def __init__(self):

		self.numbers = []
		self.winner = []
		
		self.generate_numbers()
		self.generate_winner()
	
	def generate_numbers(self):
<<<<<<< HEAD


=======
		self.numbers = []
>>>>>>> 86bd9f2d44122e7494b41469fb4674ab76be9d03
		for i in range(10):
			self.numbers.append(randint(1,10))

	def generate_winner(self):
<<<<<<< HEAD
=======
		self.winner = []
>>>>>>> 86bd9f2d44122e7494b41469fb4674ab76be9d03
		for i in range(4):
			self.winner.append(choice(self.numbers))

lotto = Lottery()

print("You are a winner if your ticket matches these numbers:", end = " ")
print(*lotto.winner, sep = " | ")
<<<<<<< HEAD
=======

>>>>>>> 86bd9f2d44122e7494b41469fb4674ab76be9d03
