input = [4, 6, 2, 9, 1]


def bubble_sort(array): # O(N^2)
    for i in range(1, len(array)):
        j = 5 - i
        for k in range(j):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!