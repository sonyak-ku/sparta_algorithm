array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2): # 이중포문을 사용한 O(N^2)을 O(N)으로 시간 복잡도를 만들기 위해서 노력함
    merge_list = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2): #while 문 사용법 익히기 !!!!
        if array1[array1_index] <= array2[array2_index]:
            merge_list.append(array1[array1_index])
            array1_index += 1
        else:
            merge_list.append(array2[array2_index])
            array2_index += 1

    return merge_list




print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!