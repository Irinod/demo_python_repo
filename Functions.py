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

# 8-10 Lists in functions

def complete_task(tasks, compl_tasks):
    while tasks:
        task = tasks.pop()
        print(f"The task {task} is now completed")
        completed_tasks = compl_tasks.append(task)


my_tasks = ["T_SQL", "Python", "Power BI", "Statistics"]
completed = []
complete_task(my_tasks[:],completed)

print(my_tasks)
print(completed)

