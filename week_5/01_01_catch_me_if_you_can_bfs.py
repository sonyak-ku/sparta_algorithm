from collections import deque

c = 11
b = 2

# 브라운의 위치 변화는 변화무쌍하다
# 이렇게 모든 경우의 수를 다 비교해야 될 때는 BFS, DFS 를 써야겠구나 라는 아이디어를 잡아야 한다.
#(선생님말씀) BFS를써야한다. 왜 D가아닌 B를 말씀하신지는 아직 잘? --> 같은 날짜 내의 모든 경우의 수를 다 비교해야하기 때문에 BFS인듯.
# BFS 는 큐 로 구현할 수있고, DFS 는 스택으로 구현할 수 있다!
# DFS 탐색을 한다고 하면, 해당 날짜에 해당되는 경우의 수들만 탐색하고 싶은데 이것들은 어떻게 해야하는 것인가?
# 규칙적인 것 저장: 배열, 자유자재로 변화하는 값 저장: 딕셔너리

def catch_me(cony_loc, brown_loc):
    visited = [{} for _ in range(200001)] #땅 20만평에, 각 땅에 방문한 시간을 전부 적어놓으려고 함
    time = 0
    que = deque()
    que.append((brown_loc, 0)) # BFS 를 위해, 큐에 자료를 넣음, 위치와 시간을 함께 넣어줌.

    while cony_loc <= 200000:
        cony_loc += time # 코니가 하루치 움직임

        #브라운이 하루치 움직임
        for i in range(0, len(que)):   # 여기까지는 나와같이 반복문이 돌때마다 3^n 으로 시간복잡도가 늘어나는 느낌을 받는다. i 는 그냥 인덱스
            cur_position, cur_time = que.popleft()
            visited[cur_position][cur_time] = True

            new_time = cur_time + 1

            new_position = cur_position - 1
            if 0 <= new_position <= 200000:
                que.append((new_position, new_time))

            new_position = cur_position + 1
            if 0 <= new_position <= 200000:
                que.append((new_position, new_time))

            new_position = cur_position * 2
            if 0 <= new_position <= 200000:
                que.append((new_position, new_time))

        if time in visited[cony_loc]: # 땅을 보고 방문한 시간중 현재 코니의 방문시각과 일치한 시간이 있다면 만난것
            return time

        time += 1  # 시간이 하루 지남

    #코니가 범위를 넘어가서 종료된 것이므로
    return '브라운과 코니는 만나지 못하게 되었습니다.'


# 쌤의 방식인데, 큐 를 사용하여 풀이를 했음에도 저 세번째는 시간이 똑같이 오래 걸린다.


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500)) # 여전히 안나옴 오래 기다려야되나본