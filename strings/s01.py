# Given a string of odd length greater than 7, 
# return a new string made of the middle three characters of a given String

# case 1 = "JhonDipPeta" - output Dip
# case 2 = "JaSonAy" - output Son

# just printing

str1 = "JhonDipPeta"

x = len(str1) // 2
new_word = str1[x - 1] + str1[x] + str1[x + 1]
print(new_word)
