def remove_letters(word, number):
    if number < 0:
        return ""

    return word[number:] 

def test_remove_letters():
    assert remove_letters("pynative", 4) == "tive"
    assert remove_letters("pynative", -1) == ""
    print("all tests passed")


test_remove_letters()
