# This is the program to practice Python classes and objects

# 9-1 Restaurant + 9-4

class Restaurant():
    '''Restaurant class'''

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # added a number served as per 9-4
    
    def describe_restaurant(self):
        print(f'{self.cuisine_type.title()} {self.restaurant_name.title()}')
    
    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name.title()} is open.')
    
    def set_number_served(self,cust_numb):
        self.number_served = cust_numb
    
    def increment_number_served(self,cust_incrmt):
        self.number_served += cust_incrmt



# Creating an object from a Restaurant class:

restaurant = Restaurant("Il patio", "italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.number_served)

# change the number of customers served:

# restaurant.number_served = 76
# print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(56)
print(restaurant.number_served)

# Calling object methods:

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2 Creating a couple more instances of Restaurant:

my_restaurant = Restaurant("Pad Thai","thai")
my_restaurant.describe_restaurant()

# 9-3 User class and 9-5

class User():
    '''Creates a User class'''

    def __init__(self, login, password, email):
        '''Initializing a User'''
        self.login = login
        self.password = password
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full information about the user \n {self.login} {self.password} {self.email}")
    
    def increment_login_attempts(self, login_incremt):
        self.login_attempts += login_incremt

    def login_attempts_reset(self):
        self.login_attempts = 0




user01 = User("US001","89013","jkl@gmail.com")
user01.describe_user()

# Increment login attempts multiple times:
print(f'Login attempts before an increment {user01.login_attempts}\n')

user01.increment_login_attempts(5)
user01.increment_login_attempts(20)

print(f'Login attempts after an increment {user01.login_attempts}\n')

# Reset the login attempts:
user01.login_attempts_reset()

print(f'Login attempts after a reset {user01.login_attempts}\n')

# 9-6 IceCreamStand

class Restaurant():
    '''Restaurant class'''

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # added a number served as per 9-4
    
    def describe_restaurant(self):
        print(f'{self.cuisine_type.title()} {self.restaurant_name.title()}')
    
    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name.title()} is open.')
    
    def set_number_served(self,cust_numb):
        self.number_served = cust_numb
    
    def increment_number_served(self,cust_incrmt):
        self.number_served += cust_incrmt



class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavours):
        super().__init__(restaurant_name,cuisine_type)

        self.flavours = flavours
    
    def add_flavours(self,flavour):
        self.flavours.append(flavour)
        
    def display_flavours(self):   
        for flav in self.flavours:
            print(f'flavour: {flav}')


my_icecream = IceCreamStand("Dolce Vitta","Gelato",["chocholate","strawberry"])
my_icecream.add_flavours("french vanilla")
my_icecream.add_flavours("pistachio")
my_icecream.add_flavours("cookies and cream")

my_icecream.display_flavours()