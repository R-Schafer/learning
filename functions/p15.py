
def text_contains_word(text, word):
    counter = 0

    for letter in text:
        if letter == word[counter]:
            counter = counter + 1

            if counter >= len(word):
                return True

        else:
            counter = 0

    return False


def test_text_contains_word():
    assert text_contains_word("hello, Emma", "hello") == True
    assert text_contains_word("hellp, Emma", "hello") == False
    assert text_contains_word(" Emma, hello", "hello") == True
    print("Works!")


test_text_contains_word()
