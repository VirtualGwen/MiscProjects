
class Restaurant:
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):

		print(f"{self.restaurant_name} {self.cuisine_type}")

	def open_restaurant(self):

		print("The restaurant is now open!")

restaurant = Restaurant("Frenchies", "French")

print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()


