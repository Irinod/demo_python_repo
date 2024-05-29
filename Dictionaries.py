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