# secret sentence
# https://dmoj.ca/problem/coci08c3p2

# After each vowel in the sentence (a, e, i, o, or u), add the letter p and that vowel again. 
# For example, rather than write down the sentence i like you, you would write ipi lipikepe yopoupu.
# Someone acquires encoded sentence. Recover the original sentence.


# creating the secret sentence
sentence = input("Enter a sentence:\n")
secret_sentence = ""
i = 0
while i < len(sentence):
    secret_sentence = secret_sentence + sentence[i]
    if sentence[i] in "aeiou":
        secret_sentence = secret_sentence + "p" + sentence[i]
        i = i + 1
    else:
        i = i + 1
        
print(f"This is the secret sentence: {secret_sentence}")


# # decoding the secret sentence
original = ""
i= 0
while i < len(secret_sentence):
    original = original + secret_sentence[i]
    if secret_sentence[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1

print(f"Here is the original sentence: {original}")

