input = "abacabade"


def find_not_repeating_character(string):
    not_repeat = []
    repeat = []
    for char in string:
        if char in repeat:
            continue
        else:
            if char not in not_repeat:
                not_repeat.append(char)
            else:
                not_repeat.remove(char)
                repeat.append(char)

    return not_repeat[0]


result = find_not_repeating_character(input)
print(result)
