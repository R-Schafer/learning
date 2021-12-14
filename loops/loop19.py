# Given a string, display only those characters which are present at an even index number.

sentence = "The brown cow walks slowing down the path"
even_character = ""
for placement in range(0, len(sentence)):
    if placement % 2 == 0:
        even_character = even_character + sentence[placement]
        
      

print(f"The sentence is: {sentence}.")
print(f"The following characters are located at the even index: {even_character}.")