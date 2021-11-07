def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for _ in string:
        if _.isalpha():
            alphabet_occurrence_array[ord(_)-97] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))