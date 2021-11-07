seat_count = 9
vip_seat_array = [4, 7]
ways_memo = {
    1: 1,
    2: 2,
    3: 3
}
# 메모이제이션을 사용하는 피보나치 수열로 풀수 있는 문제인듯
# n 개의 수가 나열되어있을 때 가짓수와 n+1 개의 수가 나열되어있을때의 가짓수를 비교 생각해보기
# 1 개가 추가된다면 가짓수가 어떻게 달라 질까? --> 피보나치 수열로 풀기 쌉가능
def get_ways_of_number(count, memo): #메모이제이션을 통한 재귀함수 사용은 원래 맞았음

    if count in memo:
        return memo[count]
    else:
        fibo_ways = get_ways_of_number(count-1, memo) + get_ways_of_number(count-2, memo)
        memo[count] = fibo_ways
        return fibo_ways




def get_all_ways_of_theater_seat(total_count, fixed_seat_array): #여기서 반복문의 오류발생
    all_ways_of_theater_seat = 1
    pole = 0
    for fixed_seat in fixed_seat_array:
            all_ways_of_theater_seat = all_ways_of_theater_seat * get_ways_of_number(fixed_seat-pole-1, ways_memo)
            pole = fixed_seat
    #최대가 9일때 vip석에 9번자리가 있을때 밑의 코드에서 파람으로 -1 이 들어가게됨, 이문제 해결부탁

    all_ways_of_theater_seat = all_ways_of_theater_seat * get_ways_of_number(total_count-pole, ways_memo)
    return all_ways_of_theater_seat

# print(get_ways_of_number(4,ways_memo))
# print(get_ways_of_number(5,ways_memo))
# print(get_ways_of_number(6,ways_memo))
# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))