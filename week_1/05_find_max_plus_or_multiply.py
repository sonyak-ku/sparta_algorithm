input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    answer = 0
    for num in array:
        if answer < 2 or num < 2:
            answer += num
        else:
            answer *= num
    return answer


result = find_max_plus_or_multiply(input)
print(result)