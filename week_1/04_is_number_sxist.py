input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):

    for char in array:
        if char == number:
            return True
    return False


result = is_number_exist(3, input)
print(result)