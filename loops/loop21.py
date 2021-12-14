# Return the count of sub-string “Emma” appears in the given string

# just printing
str = "Emma is good developer. Emma is a writer. Emma"
name = "Emma"

i = 0
j = 0

word_counter = 0

while i < len(str):
    if str[i] == name[j]:
        j = j + 1

        if j >= len(name):
            j = 0
            word_counter = word_counter + 1
    else:
        j = 0

    i = i + 1
    
print(word_counter)