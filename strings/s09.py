# Given a string, return the sum and average of the digits that appear in the string, 
# ignoring all other characters
# str1 = "English = 78 Science = 83 Math = 68 History = 65"
# Outcome:
# sum is 294
# average is 73.5

str1 = "English = 78 Science = 83 Math = 68 History = 65"
sum = 0
avg = 0
counter = 0
number = ""

for character in str1:
    if character.isnumeric():
        number = number + character
    else:
        if len(number) > 0:
            counter = counter + 1
            sum = sum + int(number)
            number = ""

if len(number) > 0:
    counter = counter + 1
    sum = sum + int(number)
            
avg = sum / counter

print(f"Sum:{sum}\nAverage:{avg}")

# another way to write this

str1 = "English = 799899 Foo = 23"
i = 0

while i < len(str1):
    if str1[i].isnumeric():
        j = i + 1
        
        while j < len(str1):
            if str1[j].isnumeric():
                j = j + 1
            else:
                break
        
        print(str1[i:j])
        i = j
    else:
        i = i + 1