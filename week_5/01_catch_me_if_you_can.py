from collections import deque

c = 11
b = 2

# 브라운의 위치 변화는 변화무쌍하다
# 이렇게 모든 경우의 수를 다 비교해야 될 때는 BFS, DFS 를 써야겠구나 라는 아이디어를 잡아야 한다.
#(선생님말씀) BFS를써야한다. 왜 D가아닌 B를 말씀하신지는 아직 잘? --> 같은 날짜 내의 모든 경우의 수를 다 비교해야하기 때문에 BFS인듯.
# BFS 는 큐 로 구현할 수있고, DFS 는 스택으로 구현할 수 있다!
# DFS 탐색을 한다고 하면, 해당 날짜에 해당되는 경우의 수들만 탐색하고 싶은데 이것들은 어떻게 해야하는 것인가?

def catch_me(cony_loc, brown_loc):
    cony_cur = cony_loc #코니의 현재위치
    brown_cur_graph = {
        0: [brown_loc] # 처음 브라운의 위치
    } #브라운의 날짜에 따른 위치찾기
    day = 1 # 날짜초기값

    while cony_cur < 200000: #코니가 해당범위를 벗어나는 순간 반복문을 종료하도록
        cony_v = 1 * day  # 코니가 이동한 거리
        cony_cur = cony_cur + cony_v  # 코니의 날짜에 따른 위치
        brown_cur_graph[day] = [] # 브라운의 날짜에 따른 위치를 넣을 공간만들기

        for brown_cur in brown_cur_graph[day-1]:  # 브라운이 움직일 수 있는 경우의수를 모두 집어넣기
            brown_ = [brown_cur - 1, brown_cur + 1, brown_cur * 2]
            if cony_cur in brown_:
                return day
            brown_cur_graph[day] = brown_cur_graph[day] + brown_

        # print(f'코니의 속도: {cony_v}, 코니의 위치: {cony_cur}')
        day += 1 # 날짜가 하루 지남


    #코니가 범위를 넘어가서 종료된 것이므로
    return '브라운과 코니는 만나지 못하게 되었습니다.'


#1. 일단 풀이의 문제도 있었고 -> 이걸 먼저 해결해 보쟝 --> 해결 끝!!
#2. 시간이 존나게 오래걸려버린다는 단점을 발견하였다. -> for문 안에서 다음 것을 넣을때 그때 확인을 하는 식으로 코드를 짠다면 불필요한 시간이 덜어질듯?
#3. 2와 연결되는 문제인데 큐를 쓰지 않았다는것이다! -> 제대로 BFS 를 구현해서 쓴다면 시간이 감축되는 결과를 보일 것으로 예상

print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 =   / 현재 풀이 값 = ", catch_me(550,500)) # 이 계산을 하지 못함, 너무 시간이 많이 걸려서.