def count_word_in_text(text, word):
    result = 0
    counter = 0

    for letter in text:
        if letter == word[counter]:
            counter = counter + 1

            if counter >= len(word):
                result = result + 1
                counter = 0
        else:
            counter = 0

    return result

print(count_word_in_text("hello emma hello", "hello"))


# similar, just compares exact strings

def comparing_words(str1, str2):
    if len(str1) != len(str2):
        return False

    for i in range(0, len(str1)):
        letter1 = str1[i]
        letter2 = str2[i]

        if letter1 != letter2:
            return False

    return True


def test_comparing_words():
    assert comparing_words("good", "good") == True
    assert comparing_words("good", "gooy") == False
    assert comparing_words("good", "goods") == False
    print("all tests passes")

test_comparing_words()
