# multiplication quiz

import pyinputplus as pyip
import random, time

# only lets the user guess a certain amount of times
# response = pyip.inputNum(limit=2)


numberOfQuestions = 10
correctAnswers = 0
for question in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = "#%s: %s x %s =" %(question, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1*num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeOutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1

    time.sleep(1)
print('Score: %s / %s' %(correctAnswers, numberOfQuestions))
