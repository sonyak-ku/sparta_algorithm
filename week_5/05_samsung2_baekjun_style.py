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

    while count < 10:
        count += 1  # 횟수 추가
        map_bfs[count] = []
        for position in map_bfs[count - 1]:
            if position in memo:
                continue # 다른 차수에서 똑같은 위치가 있었다면 건너뛰기
            else: # 처음 보는 레드 블루 공의 배치일 때
                memo.append(position)
                # 상, 하, 좌, 우 기울기배치해서 공의 움직임을 map_bfs 에 저장해야한다.
                B_in_hole, R_in_hole, new_position = upper_tilt(game_map, position, answer)

                if not B_in_hole: # 파란 공이 빠지지 않은 경우
                    if R_in_hole:
                        return count
                    else: # 파란 공도 빨간 공도 구멍에 빠지지 않은 경우
                        map_bfs[count].append(new_position)

                B_in_hole, R_in_hole, new_position = lower_tilt(game_map, position, answer)

                if not B_in_hole:  # 파란 공이 빠지지 않은 경우
                    if R_in_hole:
                        return count
                    else:  # 파란 공도 빨간 공도 구멍에 빠지지 않은 경우
                        map_bfs[count].append(new_position)

                B_in_hole, R_in_hole, new_position = left_tilt(game_map, position, answer)

                if not B_in_hole:  # 파란 공이 빠지지 않은 경우
                    if R_in_hole:
                        return count
                    else:  # 파란 공도 빨간 공도 구멍에 빠지지 않은 경우
                        map_bfs[count].append(new_position)

                B_in_hole, R_in_hole, new_position = right_tilt(game_map, position, answer)

                if not B_in_hole:  # 파란 공이 빠지지 않은 경우
                    if R_in_hole:
                        return count
                    else:  # 파란 공도 빨간 공도 구멍에 빠지지 않은 경우
                        map_bfs[count].append(new_position)

                # 여기서 성공실패조건 체크해야 됨 - 리턴된 red_ball_in_hole 변수로 체크

    return -1

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
            if map[nr][ny] != '#': # 빨간 공이 이동하려는 곳에 벽이 없을 때
                cur_R = [nr, ny]
                if cur_R == answer:
                    red_ball_in_hole = True
                    cur_R = [-1, -1]
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
                    cur_R = [-1, -1]
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
                    cur_R = [-1, -1]
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
                    cur_R = [-1, -1]
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

tr, ty = map(int, input().split())

map = [[i for i in input()] for r in range(tr)]

print(is_available_to_take_out_only_red_marble(map))
## map 함수 사용하기 : map(적용할 함수, iter자료형)음

#빨간공이 먼저 움직이고 파란공이 연달아 있을때 빨간 공이 빠지고, 그자리가 비어서 파란공이 연달아 빠지는 것을 구현해야 된다 -> 동그라미에 빠지면 맵상에 공이 사라지는 느낌 구현
# 9 6
######
##.#.#
#.#.##
#..#.#
#B..##
#R#.##
#.##.#
#O.###
######