# This is the program to practice Python classes and objects

# 9-1 Restaurant

class Restaurant():
    '''Restaurant class'''

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'{self.cuisine_type.title()} {self.restaurant_name.title()}')
    
    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name.title()} is open.')


# Creating an object from a Restaurant class:

restaurant = Restaurant("Il patio", "italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling object methods:

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2 Creating a couple more instances of Restaurant:

my_restaurant = Restaurant("Pad Thai","thai")
my_restaurant.describe_restaurant()