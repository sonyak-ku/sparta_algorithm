input = [4, 6, 2, 9, 1]


def insertion_sort(array): #break문이 추가로 있기 때문에 굳이 이중 for문이 안돌아도 되는 경우에서는 안 돌기 때문에
    #선택 버블 보다 효율적일 수 있음, 최선의 경우 O(N) 의 시간복잡도가 소요
    sorted_list = []
    for i in array:
        sorted_list.append(i)
        for j in range(1, len(sorted_list)):
            if sorted_list[-j] < sorted_list[-j-1]:
                sorted_list[-j], sorted_list[-j-1] = sorted_list[-j-1], sorted_list[-j]
                print('if', sorted_list[-j], sorted_list[-j-1])
                print(sorted_list)
            else:
                print('break')
                break

    return sorted_list


print(insertion_sort(input))
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!