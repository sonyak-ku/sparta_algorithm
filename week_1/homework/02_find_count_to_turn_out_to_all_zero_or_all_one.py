from collections import Counter

input = "01011110100"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 뭉쳐진 덩이가 가장 적은 애들을 뒤집어야 한다 > 일렬로 나열된 된애들을 제거하기 > 적은 개수(0 또는 1)가 답
    remove_next_same = ''
    pre = ''
    for char in string:
        if char == pre:
            continue
        else:
            remove_next_same += char
        pre = char

    # Counter(remove_next_same).most_common() -> [('0', 4), ('1', 3)]
    # 0 과 1 두 숫자 밖에 없고, 빈도가 높은 숫자부터 작은 숫자 순서로 표현해줘서, 빈도가 작은 숫자의 빈도를 [1][1] 으로 얻을 수 있다
    return Counter(remove_next_same).most_common()[1][1]


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)