# relative path if youre in the same folder
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# absolute path
file_path = '/home/rschafer/learning/ttt/filetest.txt'
with open(file_path) as file_object:
    print(file_object.read())

# relative path
file_path = '../ttt/filetest.txt'
with open(file_path) as file_object:
    print(file_object.read())


# looping over a file to read line by line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)


# If you want to retain access to a file’s contents outside the with block, 
# you can store the file’s lines in a list inside the block and then work with that list.
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
       print(line.rstrip())

# reading cats.txt and dogs.txt for "try it yourself"
filename = 'cats.txt'
with open(filename) as file_object:
    print(file_object.read())
# if i move the dogs.txt file I should make a try and except to tell me its not in the correct spot
try:
    filename = 'dogs.txt'
    with open(filename) as file_object:
        print(file_object.read())
except FileNotFoundError:
    print("File is not located in files1 folder")

    
