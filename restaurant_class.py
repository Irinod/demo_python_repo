# This module contains the Restaurant class definition


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
