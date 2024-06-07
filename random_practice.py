# This file contains practice exercises for random standard module

# my_number = randint(1,6)
# print(my_number)

# meal_plan = ["spagetti", "Dumplings", "Burrito", "Tacos"]

# my_meal = choice(meal_plan)
# print(f'today I am going to have: {my_meal}')

# 9-13 Dice

# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint, choice

class Die():
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1,self.sides))



# Create a die with 6 sides (default)
die6 = Die()

for i in range(1,11):
    die6.roll_die()


# Create a die with 10 sides
die10 = Die(10)

for i in range(1,11):
    die10.roll_die()


# Create a die with 20 sides
die20 = Die(20)

for i in range(1,11):
    die20.roll_die()