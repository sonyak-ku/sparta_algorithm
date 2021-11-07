finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    cp_numbers = numbers
    cp_numbers.sort()
    start = 0
    end = len(numbers) - 1
    count = 0
    is_exist = False

    while start < end:
        if cp_numbers[(start + end) // 2] == target:
            print(cp_numbers[(start + end) // 2], 'if')
            return True

        elif cp_numbers[(start + end) // 2] > target:
            print(cp_numbers[(start + end) // 2], 'elif')
            end = cp_numbers[(start + end) // 2]
            count += 1
        else:
            print(cp_numbers[(start + end) // 2], 'else')
            start = cp_numbers[(start + end) // 2]
            count += 1
    return is_exist





result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
# finding_numbers.sort() #리턴값이 없다
# print(finding_numbers)