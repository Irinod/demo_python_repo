# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country.

def city_country(city_name, country_name):
    '''This function combines city and country names'''
    return f"{city_name} {country_name}".title()


print(city_country("moscow","russia"))

# 8-7 Make album

def make_album(album_name, artist, num_songs = None):
    return {'album_title': album_name, 'artist': artist, 'num_songs': num_songs}


alb1 = make_album("Staying alive", "Bee Gees")
alb2 = make_album("Nevermind", "Nirvana", 20)

print(alb1)
print(alb2)
