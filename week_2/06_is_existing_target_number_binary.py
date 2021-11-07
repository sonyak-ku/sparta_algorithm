finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    start = 0
    end = len(array)-1
    count = 0
    is_exist = False

    while start < end:
        if array[(start + end)//2] == target:
            print(array[(start + end) // 2], 'if')
            return True

        elif array[(start + end)//2] > target:
            print(array[(start + end)//2], 'elif')
            end = array[(start + end) // 2]
            count += 1
        else:
            print(array[(start + end) // 2], 'else')
            start = array[(start + end) // 2]
            count += 1
    return is_exist


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)