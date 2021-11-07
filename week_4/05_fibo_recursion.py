input = 20


def fibo_recursion(n): #input 이 커질수록 시간이 아주~~오래 걸린다는 문제
    # 구현해보세요!
    if n < 1:   #얘가 필요가 없을 수도 있겟다?
        return
    if n <= 2:
        return 1

    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765