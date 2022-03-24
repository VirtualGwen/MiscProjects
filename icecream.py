import diner

restaurant = diner.Restaurant("Stuart's", "Ice Cream")

print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
