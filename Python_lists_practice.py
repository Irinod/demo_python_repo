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

# Print an invite for the remaining 2 guests

for guest in my_guests:
    print(f'{guest.title()}, please come along!\n')