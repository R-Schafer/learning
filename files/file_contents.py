filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# printing a much larger pi
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


# is my birthday located in pi
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    line = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = "022389"
if birthday in pi_string:
    print("your birthday appears in pi")
else:
    print("your birthday is not in pi")

# using the replace method()
message = "I like cats"
print(message.replace('cats', 'dogs'))
