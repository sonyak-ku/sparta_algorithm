array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2): # 이중포문을 사용한 O(N^2)을 O(N)으로 시간 복잡도를 만들기 위해서 노력함
    merged_list = []
    count_1, count_2 = 0, 0
    max_1, max_2 = len(array1)-1, len(array2)-1
    times = len(array1) + len(array2)

    for time in range(times):
        if array1[count_1] >= array2[count_2]:
            merged_list.append(array2[count_2])
            if count_2 < max_2:
                count_2 += 1
                print(count_2, max_2)
            elif count_2 == max_2:
                return merged_list + array1[count_1:]

        else:
            merged_list.append(array1[count_1])
            if count_1 < max_1:
                count_1 += 1
                print(count_1, max_1)
            elif count_1 == max_1:
                print(count_2)
                return merged_list + array2[count_2:]





print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!