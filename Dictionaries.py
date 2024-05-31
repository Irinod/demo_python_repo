# This file is for practicing Dictionaries
# 6-1 Persona

persona = {
    "name":"Rob",
    "last name":"Dominikovich",
    "age":55,
    "city":"Waiheke Island"
}

for attrib,val in persona.items():
    print(attrib)
    print(val)

# 6-2 Favorite numbers

fav_numb = {
    "irina":23,
    "elena":15,
    "rob":42,
    "leo":10,
    "sam":50
}

for f in fav_numb.keys():
    print(f)
    print(fav_numb.get(f))

# 6-3 Glossary

glossary = {
    "kurtosis":"weight of tails",
    "skeweness":"assymetry",
    "tiebreaker":"deciding identifier"
}

for term in glossary:
    print(f"The new word is: {term}. It means {glossary[term]}")

# 6-4 Glossary 2

glossary2 = {
    "kurtosis":"weight of tails",
    "skeweness":"assymetry",
    "tiebreaker":"deciding identifier"
}

my_dict_words = glossary2.keys()
my_dict_meanings = glossary2.values()

glossary2["normality"] = "normal distribution"
glossary2["mean"] = "average"

print(my_dict_words)
print(my_dict_meanings)

# 6-5 River-Coutnry

rivers = {
    "volga" : "russia",
    "nile" : "egypt",
    "danube": "germany"
}

for river in rivers:
    print(f"River {river.title()} flows through {rivers[river].title()}")

# 6-6 Languages

fav_language = {
    "irina":"python",
    "rob":"sas",
    "dima":"C sharp",
    "lena":"C sharp"
}

# print only unique languages

for langg in set(fav_language.values()):
    print(langg)

# 6-7 People

person1 = {
    "name":"ira",
    "age":25
}

person2 = {
    "name":"lena",
    "age":25
}

person3 = {
    "name":"galya",
    "age":25
}

fam_list = []
fam_list.append(person1)
fam_list.append(person2)
fam_list.append(person3)

for member in fam_list:
    print(member)

# 6-9 Favorite places

fav_places = {
    "irina":["dacha", "Paris"],
    "lena":["seversk"],
    "galya":["tomsk","barnaul"]
}

for member,place in fav_places.items():
    print(f"Family member name: {member}\n")
    
    for item in place:
        print(f"Favorite place: {item}\n")


# Recursion example

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)