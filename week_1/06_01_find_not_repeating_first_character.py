from collections import Counter

input = "abadabace"


def find_not_repeating_character(string):

    obj = Counter(string).most_common()
    return obj
    # for tup in obj:
    #     if tup[1] == 1:
    #         return tup[0]

    # set(string) #순서가 없다 set은


result = find_not_repeating_character(input)
print(result)
