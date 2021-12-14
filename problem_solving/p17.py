# Ptice
# https://dmoj.ca/problem/coci08c1p2


questions = int(input("How many questions on the exam:\n"))
correct_answers = input("Enter the correct answers:\n")

Adrian = "ABC"
Adrian_correct = 0

Bruno = "BABC"
Bruno_correct = 0

Gordan = "CCAABB"
Gordan_correct = 0

for i in range(0, questions):
    ai = i % len(Adrian)
    if Adrian[ai] == correct_answers[i]:
        Adrian_correct += 1

    bi = i % len(Bruno)
    if Bruno[bi] == correct_answers[i]:
        Bruno_correct += 1
    
    gi = i % len(Gordan)
    if Gordan[gi] == correct_answers[i]:
        Gordan_correct += 1

print(f"Adrian: {Adrian_correct} out of {questions}")
print(f"Bruno: {Bruno_correct} out of {questions}")
print(f"Gordan: {Gordan_correct} out of {questions}")