# odd numbers from the first list
# even numbers from the second list


def numbers_in_list(list1, list2):
    new_list = []

    for num in list1:
        if num % 2 != 0:
            new_list.append(num)

    for num in list2:
        if num % 2 == 0:
            new_list.append(num)

    return new_list


def test_numbers_in_list():
    assert numbers_in_list([10, 20, 23, 11, 17], [13, 43, 24, 36, 12]) == [
        23,
        11,
        17,
        24,
        36,
        12,
    ]
    assert numbers_in_list([11, 20, 23, 11, 17], [13, 43, 24, 36, 12]) == [
        11,
        23,
        11,
        17,
        24,
        36,
        12,
    ]
    print("✅")


test_numbers_in_list()
