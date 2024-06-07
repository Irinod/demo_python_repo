# This program imports Restaurant class from restaurant_class module

import importlib.util
 
# specify the module that needs to be 
# imported relative to the path of the 
# module
spec=importlib.util.spec_from_file_location("restaurant_class","C:\Users\irina\OneDrive\Desktop\GIT Repos\git\demo_python_repo\demo_python_repo\restaurant_class.py")
 


from restaurant_class import Restaurant


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