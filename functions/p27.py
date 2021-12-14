# reversing a string

def get_string():
    return input("Write a sentence:\n")
    
def splitting_words(sentence):
    words = []
    new_word = ""
    for i in sentence:
        if i != " ":
            new_word = new_word + i
        elif i == " " and new_word != "":
            words.append(new_word)
            new_word = ""
    
    if new_word != "":
        words.append(new_word)
        
    return words
            
def reverse_string(words):
    new_sentence = ""
    for i in range(len(words) - 1, - 1, - 1):
        new_sentence  = new_sentence + words[i] + " "
        
    return new_sentence

def main():
    sentence = get_string()
    words = splitting_words(sentence)
    print(reverse_string(words))

main()




