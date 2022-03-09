import random
import time

class Dice:
	def __init__(self, sides):
		self.sides = sides

	def die_sides(sides):
		self.sides = sides

def main():
	random.seed(time.time())

	die = Dice(6)

	r = random.randint(1,die.sides)

	print("Using a {} sided die, you have rolled {}".format(die.sides, r))

if __name__ == "__main__":
	main()
