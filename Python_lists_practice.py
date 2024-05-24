# This is my practice file to master Lists in Python
# I am going to complete all excercises provided in Python Crash Course book

# 3-1
my_friends = ['rob', 'yeliz', 'adam']

for friend in my_friends:
    print(f'{friend.title()}')

# 3-2
my_friends = ['rob', 'yeliz', 'adam']

for friend in my_friends:
    print(f'How are you doing, {friend.title()}?')

# 3-3
wish_list = ['house', 'car', 'trip', 'furniture']

for wish in wish_list:
    print(f'I would like to own a {wish}')

# 3-4 and 5 Invite to dinner
my_guests = ['mom', 'rob', 'leo']

i = 0
for guest in my_guests:
    if guest == 'mom':
        my_guests[i] = 'mother'
    
    print(f'I"d like to invite you to dinner, {my_guests[i].title()}!')
    i += 1

# 3-6 extend invitation to more guests
my_guests = ['mom', 'rob', 'leo']

my_guests.insert(0, 'catherine')
my_guests.insert(2, 'mike')
my_guests.append('tracey')
print(my_guests)

for guest in my_guests:
    print(f'We now have a bigger table!')
    print(f'{guest.title()}, please come along!\n')

# 3-7 Shrinking Guest List
# I can now only invite 2 people from a guest list

my_guests = ['mom', 'rob', 'leo', 'tracey', 'mike']

for guest in my_guests:
    print(f'Apologies, {guest.title()}, I can only invite 2 people')


# Removing guests from the list until only 2 left

while len(my_guests) > 2:
    guest_rem = my_guests.pop()
    print(f'Apologies, {guest_rem.title()}, dinner got cancelled')

print(my_guests)
# Print an invite for the remaining 2 guests

for guest in my_guests:
    print(f'{guest.title()}, please come along!\n')

# use del to remove the last 2 people from the list
# and leave it empty

print(my_guests)

while len(my_guests) == 0:
    del my_guests[i]

print(my_guests)

# 3-8 Temp sorting vs Permanent sorting
locations = ['Italy', 'Spain', 'Germany', 'Danmark']

# Temp sort with sorted()
print(f'original list \n {locations}')

# Sort in ascending order with sorted()
print(f'temp ascending order \n {sorted(locations)}')

# Sort in descending order with sorted()
print(f'temp descending order \n {sorted(locations, reverse=True)}')

# Original list hasn't changed:
print(f'\n original list \n {locations}')

# Permanent reverse order
locations.reverse()
print(f'\n the order has permanently changed:\n {locations}')

# Permanent sort order

print(f'\n original list \n {locations}')
locations.sort(reverse=True)
print(f'\n the order has permanently changed:\n {locations}')

# 3-9 add number of people invited
my_guests = ['mom', 'rob', 'leo', 'tracey', 'mike']
num_guests = len(my_guests)

for guest in my_guests:
    print(f'There are {num_guests} of us confirmed')
    print(f'{guest.title()}, please come along!\n')

# 4-1 Pizza 
fav_pizza = ['margarita', 'marinara', 'roman']

for pizza in fav_pizza:
    print(f'I like {pizza} pizza')

print('I like freshly made pizza\n It has to have lots of vegies in it')

# 4-2 Pets

animals = ['dog', 'cat', 'snake']

for animal in animals:
    print(f'{animal.title()} would make a good pet!')

print('\nAny of these animals would make a good pet!')

# 4-3 print numbers from 1 to 20 incl.
for i in range(1,21):
    print(i)


# 4-4 List from numbers
num_list = list(range(1,11))
print(num_list)

# 4-5 Summing a million
num_list_huge = list(range(1,1000001))

list_min = min(num_list_huge)
print(list_min)
print('\n')

list_max = max(num_list_huge)
print(list_max)
print('\n')

list_sum = sum(num_list_huge)
print(list_sum)

# 4-6 Odd numbers from 1 to 20
# solution 1 - using list() and range()
odd_numb1 = list(range(1,21,2))
print(odd_numb1, '\n')

# solution 2 - using list comprehension and range()
odd_numb2 = [numb for numb in range(1,21,2)]
print(odd_numb2, '\n')

