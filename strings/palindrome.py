# is the string a palindrome

word = input("Enter a word:\n")
reverse_word = ""

reverse_word = word[::-1]
    
if reverse_word == word:
    print("This is a palindrome")
else:
    print("Not a palindrome")


