# 10-1 Read file into a list

file_path = 'C:/Users/irina/AppData/Local/Programs/Python/Python310/files/learning_python.txt'

with open(file_path) as filename:
    lines = filename.readlines()


for line in lines:
    print(line)


# 10-2 Use Replace() method

file_path = 'C:/Users/irina/AppData/Local/Programs/Python/Python310/files/learning_python.txt'

with open(file_path) as filename:
    lines = filename.readlines()


for line in lines:
    line.replace("can", "should")
    print(line)

# writing to a file 

file_path = 'C:/Users/irina/AppData/Local/Programs/Python/Python310/files/programming.txt'

with open(file_path, 'w') as filename:
    filename.write("I love programming")

with open(file_path) as filename:
    lines = filename.readlines()

for line in lines:
    print

# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

