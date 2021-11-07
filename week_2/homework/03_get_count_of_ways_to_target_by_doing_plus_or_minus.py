from itertools import combinations

numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    minus = (sum(array) - target)//2
    plus = len(array) - minus
    plus_and_minus = plus*'+' + minus*'-'

    return len(list(combinations(plus_and_minus, minus)))


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!

# a = itertools.combinations('abcde', 1)
# print(list(a))