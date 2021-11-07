input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max = 0
    for _ in array:
        if max < _:
            max = _
    return max


result = find_max_num(input)
print(result)
