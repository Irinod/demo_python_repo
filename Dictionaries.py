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