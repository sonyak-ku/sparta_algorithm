input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    occurence = [0] * 26
    for char in string:
        if char.isalpha():
            occurence[ord(char) - 97] += 1

    max_index = occurence.index(max(occurence))


    return chr(max_index + 97)


result = find_max_occurred_alphabet(input)

print(result)