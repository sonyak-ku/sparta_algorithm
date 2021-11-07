from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

### 백준의 테스트 케이스를 통해 코드의 문제가 뭔지 더 자세히 알 수 있음
def is_available_to_take_out_only_red_marble(game_map):
    cur_R, cur_B, answer = [], [], [] # 좌표찾기
    for i, row in enumerate(game_map):
        for j, y in enumerate(row):
            if y == 'R':
                cur_R += [i, j]
            elif y == 'B':
                cur_B += [i, j]
            elif y == 'O':  # 빨간공이 들어가야 할 구멍
                answer += [i, j]
    map_bfs = {  # 탐색용
        0: [
            {'R': cur_R, 'B': cur_B}
        ]
    }
    memo = [] # 메모 탐색
    count = 0 # 횟수체크  10 이 넘어가면 리턴

    while count < 11:
        map_bfs[count + 1] = []
        for position in map_bfs[count]:
            if position in memo:
                continue # 다른 차수에서 똑같은 위치가 있었다면 건너뛰기
            else: # 처음 보는 레드 블루 공의 배치일 때
                memo.append(position)
                # 상, 하, 좌, 우 기울기배치해서 공의 움직임을 map_bfs 에 저장해야한다.
                B_in_hole, R_in_hole, new_position = upper_tilt(game_map, position, answer)
                print('fin upper')
                if not B_in_hole: # 파란 공이 빠지지 않은 경우
                    if R_in_hole:
                        return count < 11
                    else: # 파란 공도 빨간 공도 구멍에 빠지지 않은 경우
                        map_bfs[count + 1].append(new_position)

                B_in_hole, R_in_hole, new_position = lower_tilt(game_map, position, answer)
                print('fin lower')
                if not B_in_hole:  # 파란 공이 빠지지 않은 경우
                    if R_in_hole:
                        return count < 11
                    else:  # 파란 공도 빨간 공도 구멍에 빠지지 않은 경우
                        map_bfs[count + 1].append(new_position)

                B_in_hole, R_in_hole, new_position = left_tilt(game_map, position, answer)
                print('fin left')
                if not B_in_hole:  # 파란 공이 빠지지 않은 경우
                    if R_in_hole:
                        return count < 11
                    else:  # 파란 공도 빨간 공도 구멍에 빠지지 않은 경우
                        map_bfs[count + 1].append(new_position)

                B_in_hole, R_in_hole, new_position = right_tilt(game_map, position, answer)
                print('fin right')
                if not B_in_hole:  # 파란 공이 빠지지 않은 경우
                    if R_in_hole:
                        return count < 11
                    else:  # 파란 공도 빨간 공도 구멍에 빠지지 않은 경우
                        map_bfs[count + 1].append(new_position)

                # 여기서 성공실패조건 체크해야 됨 - 리턴된 red_ball_in_hole 변수로 체크

        count += 1 # 횟수 추가



    return False

## 실패조건 잘 생각해야된다, 파랑 공이 구멍으로 빠진다
## 성공조건 어떻게 생각해야되는지 체크

def upper_tilt(map, position, answer): # 맵의 정보가 있어야 한다. 각 공의 위치가 있어야 한다. 구멍의 위치 정보 있어야 한다. ## 맵의 정보가 변해야 한다.
    cur_R, cur_B = position['R'], position['B']  # 리스트 형태 위치좌표 [r, y]
    new_position = {}
    blue_ball_in_hole = False # 파란 공이 빠진지 체크
    red_ball_in_hole = False # 빨간 공 구멍에 빠져서
    # 위로 기울이니깐 더 위에 있는 애가 먼저 이동해야 while문으로 돌려야 됨.
    R_not_meet_wall, B_not_meet_wall = True, True
    while R_not_meet_wall or B_not_meet_wall: # 둘중에 하나라도 벽을 만나지 않았으면 기울기는 지속되기
        if cur_R[0] <= cur_B[0]: # 빨간 공 먼저 이동

            nr, ny = cur_R[0] - 1, cur_R[1]
            if  map[nr][ny] != '#': # 빨간 공이 이동하려는 곳에 벽이 없을 때
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True
            else: # 빨간 공이 벽을 만났을 때
                R_not_meet_wall = False

            nr, ny = cur_B[0] - 1, cur_B[1]
            if map[nr][ny] != '#' and [nr, ny] != cur_R: # 파란 공이 이동하려는 곳에 벽과 빨간공이 없을 때
                cur_B = [nr, ny]
                if cur_B == answer:
                    blue_ball_in_hole = True
            else: # 파란 공이 벽(다른 공 포함)을 만났을 때
                B_not_meet_wall = False

        else:

            nr, ny = cur_B[0] - 1, cur_B[1] #파란공
            if map[nr][ny] != '#':  # 파란 공이 이동하려는 곳에 벽이 없을 때
                cur_B = [nr, ny]
                if cur_B == answer:
                    blue_ball_in_hole = True
            else:
                B_not_meet_wall = False

            nr, ny = cur_R[0] - 1, cur_R[1]
            if map[nr][ny] != '#' and [nr, ny] != cur_B:  # 빨간공 이동에 파란공없어야
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True
            else:  # 빨간 공이 벽을 만났을 때
                R_not_meet_wall = False


    new_position['R'] = cur_R
    new_position['B'] = cur_B

    return [blue_ball_in_hole, red_ball_in_hole, new_position] # 기울였을 때, 공들의 위치를 반환하는 함수로

def lower_tilt(map, position, answer):
    cur_R, cur_B = position['R'], position['B']  # 리스트 형태 위치좌표 [r, y]
    new_position = {}
    blue_ball_in_hole = False  # 파란 공이 빠진지 체크
    red_ball_in_hole = False  # 빨간 공 구멍에 빠져서
    # 아래로 기울이니깐 더 위에 있는 애가 먼저 이동해야 while문으로 돌려야 됨.
    R_not_meet_wall, B_not_meet_wall = True, True
    while R_not_meet_wall or B_not_meet_wall:  # 둘중에 하나라도 벽을 만나지 않았으면 기울기는 지속되기
        if cur_R[0] >= cur_B[0]:  # 빨간 공이 더 아래에 있으니 먼저 아래로 떨어지라는 느낌

            nr, ny = cur_R[0] + 1, cur_R[1]
            if map[nr][ny] != '#':  # 빨간 공이 이동하려는 곳에 벽이 없을 때
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True
            else:  # 빨간 공이 벽을 만났을 때
                R_not_meet_wall = False

            nr, ny = cur_B[0] + 1, cur_B[1]
            if map[nr][ny] != '#' and [nr, ny] != cur_R:  # 파란 공이 이동하려는 곳에 벽과 빨간공이 없을 때
                cur_B = [nr, ny]
                if cur_B == answer:
                    blue_ball_in_hole = True
            else:  # 파란 공이 벽(다른 공 포함)을 만났을 때
                B_not_meet_wall = False

        else:  # B가 더 아래에있는 공일때

            nr, ny = cur_B[0] + 1, cur_B[1]
            if map[nr][ny] != '#':  # 파란 공이 이동하려는 곳에 벽이 없을 때
                cur_B = [nr, ny]
                if cur_B == answer:
                    blue_ball_in_hole = True
            else:
                B_not_meet_wall = False

            nr, ny = cur_R[0] + 1, cur_R[1]
            if map[nr][ny] != '#' and [nr, ny] != cur_B:  # 빨간 공이 이동하려는 곳에 벽과 파란공이이 없을 때
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True
            else:  # 빨간 공이 벽을 만났을 때
                R_not_meet_wall = False

    new_position['R'] = cur_R
    new_position['B'] = cur_B

    return [blue_ball_in_hole, red_ball_in_hole, new_position]  # 기울였을 때, 공들의 위치를 반환하는 함수로

def left_tilt(map, position, answer):
    cur_R, cur_B = position['R'], position['B']  # 리스트 형태 위치좌표 [r, y]
    new_position = {}
    blue_ball_in_hole = False  # 파란 공이 빠진지 체크
    red_ball_in_hole = False  # 빨간 공 구멍에 빠져서
    # 위로 기울이니깐 더 위에 있는 애가 먼저 이동해야 while문으로 돌려야 됨.
    R_not_meet_wall, B_not_meet_wall = True, True
    while R_not_meet_wall or B_not_meet_wall:  # 둘중에 하나라도 벽을 만나지 않았으면 기울기는 지속되기
        if cur_R[1] <= cur_B[1]:  # 빨간공이 더 왼쪽에 있을 때

            nr, ny = cur_R[0], cur_R[1] - 1
            if map[nr][ny] != '#':  # 빨간 공이 이동하려는 곳에 벽이 없을 때
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True
            else:  # 빨간 공이 벽을 만났을 때
                R_not_meet_wall = False

            nr, ny = cur_B[0], cur_B[1] - 1
            if map[nr][ny] != '#' and [nr, ny] != cur_R:  # 파란 공이 이동하려는 곳에 벽과 빨간공이 없을 때
                cur_B = [nr, ny]
                if cur_B == answer:
                    blue_ball_in_hole = True
            else:  # 파란 공이 벽(다른 공 포함)을 만났을 때
                B_not_meet_wall = False

        else:  # B가 더 왼쪽에있는 공일때

            nr, ny = cur_B[0], cur_B[1] - 1
            if map[nr][ny] != '#':  # 파란 공이 이동하려는 곳에 벽이 없을 때
                cur_B = [nr, ny]
                if cur_B == answer:
                    blue_ball_in_hole = True
            else:
                B_not_meet_wall = False

            nr, ny = cur_R[0], cur_R[1] - 1
            if map[nr][ny] != '#' and [nr, ny] != cur_B:  # 빨간 공이 이동하려는 곳에 벽과 파란공이이 없을 때
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True
            else:  # 빨간 공이 벽을 만났을 때
                R_not_meet_wall = False

    new_position['R'] = cur_R
    new_position['B'] = cur_B

    return [blue_ball_in_hole, red_ball_in_hole, new_position]  # 기울였을 때, 공들의 위치를 반환하는 함수로

def right_tilt(map, position, answer):
    cur_R, cur_B = position['R'], position['B']  # 리스트 형태 위치좌표 [r, y]
    new_position = {}
    blue_ball_in_hole = False  # 파란 공이 빠진지 체크
    red_ball_in_hole = False  # 빨간 공 구멍에 빠져서
    # 위로 기울이니깐 더 위에 있는 애가 먼저 이동해야 while문으로 돌려야 됨.
    R_not_meet_wall, B_not_meet_wall = True, True

    while R_not_meet_wall or B_not_meet_wall:  # 둘중에 하나라도 벽을 만나지 않았으면 기울기는 지속되기
        if cur_R[1] >= cur_B[1]:  # 빨간공이 더 오른쪽에 있을 때

            nr, ny = cur_R[0], cur_R[1] + 1
            if map[nr][ny] != '#':  # 빨간 공이 이동하려는 곳에 벽이 없을 때
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True
            else:  # 빨간 공이 벽을 만났을 때
                R_not_meet_wall = False

            nr, ny = cur_B[0], cur_B[1] + 1
            if map[nr][ny] != '#' and [nr, ny] != cur_R:  # 파란 공이 이동하려는 곳에 벽과 빨간공이 없을 때
                cur_B = [nr, ny]
                if cur_B == answer:
                    blue_ball_in_hole = True
            else:  # 파란 공이 벽(다른 공 포함)을 만났을 때
                B_not_meet_wall = False

        else:  # B가 더 왼쪽에있는 공일때

            nr, ny = cur_B[0], cur_B[1] + 1
            if map[nr][ny] != '#':  # 파란 공이 이동하려는 곳에 벽이 없을 때
                cur_B = [nr, ny]
                if cur_B == answer:
                    blue_ball_in_hole = True
            else:
                B_not_meet_wall = False

            nr, ny = cur_R[0], cur_R[1] + 1
            if map[nr][ny] == '#' or [nr, ny] == cur_B: # 벽이거나 파란 공과 겹칠때
                R_not_meet_wall = False
            else: #겹치는게 아니라면
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True


    new_position['R'] = cur_R
    new_position['B'] = cur_B

    return [blue_ball_in_hole, red_ball_in_hole, new_position]  # 기울였을 때, 공들의 위치를 반환하는 함수로


# print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다

#### 이 문제가 되게 나에게는 난이도가 높다는 것을 알고있고, 머리로는 생각할 수 있는 풀이 방식을 그대로 코드로 내가 구현할 수 있는지에 대한 지금 망설임이 든다.
#### 하지만 일단 해봐야 되는 것이고, 이 문제를 풀게 된다면 또한번 성장을 했다는 뜻이니깐, 그리고 머릿속에 풀이 방법이 그려지는게 어느정도 자신은 있고.
## 내 풀이 방식은 공들을 기울이다가 구멍을 지나가는지를 체크해서 푸는 것이다. 따라서 문제풀이는 할 수 있지만 완전한 문제 풇이는 아닌듯 ( 약간 가라로 푸는것이라 ) 제대로 다른 방식으로 풀어보기
game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))