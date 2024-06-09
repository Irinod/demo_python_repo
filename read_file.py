
file_path = 'C:/Users/irina/AppData/Local/Programs/Python/Python310/files/pi_file.txt'
with open(file_path) as file_object:
    contents = file_object.read()

print(contents)

# Reading a text file line-by-line

file_path = 'C:/Users/irina/AppData/Local/Programs/Python/Python310/files/pi_file.txt'

with open(file_path) as filename:
    for line in filename:
        print(line)