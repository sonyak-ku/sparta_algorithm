input = 90


def find_prime_list_under_number(number):
    prime_number = []
    for num in range(2, number+1):

        for prime_num in prime_number:
            if num % prime_num == 0 and prime_num * prime_num <= num:
                print(f"{num} : {prime_num}")
                break #소수 그룹내의 숫자로 나뉘어 질 경우
                #내가 이해가 안되는 부분은, break 더 빨리 떠야지 연산 개수가 줄게 되는 건데
                #break 뜨는 조건을 이렇게 빡빡하게 하나 추가하면 break가 과연 더 빨리 뜰까? 라는 의문?
                #효율성 제고에 과연 도움이 되는게 맞는가?
        else:  #for-else문, 위의 for 문에서 break가 없으면 넘어오게됨
            prime_number.append(num)

    return prime_number
 

result = find_prime_list_under_number(input)

print(result)