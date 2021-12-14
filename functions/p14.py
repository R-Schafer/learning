def exponent(base, exp):
    total = 1
    for i in range(1, exp + 1):
        total = total * base
    return total


def test_exponent():
    assert exponent(2, 5) == 32
    assert exponent(5, 4) == 625
    print("works!")


test_exponent()
