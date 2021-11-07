input = [4, 6, 2, 9, 1]


def selection_sort(array): # O(N^2)
    max_index = 0
    n = len(array)
    for i in range(1, n):
        for j in range(5-i):
            if array[max_index] < array[j]:
                max_index = j
        array[max_index], array[n - i] = array[n - i], array[max_index]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!