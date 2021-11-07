from collections import deque

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

## 좋은 트릭, 체스판의 주변을 모두 blue 로 만들면 벽을 만난다는 케이스를 뛰어넘기가 가능하다.
### 첫번째 오류, 기본적인 작동은 잘 되었지만, 자기 턴에서 움직인게 아니라, 남의 턴에서 업혀서 움직였을 때 위치 정보 갱신이 이루어지지 않았기 때문에 오류 생김.

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    new_map = surround_blue_wall(game_map) # 전체를 파란보드로 둘러싸서 편하게 플레이하기 위함
    horse_info = horse_location_and_directions
    for i in horse_location_and_directions: # 맵을 둘러 쌓았기 때문에 생기는 위치 변화 체크
        i[0] += 1
        i[1] += 1
    current_board = [[[] for j in range(len(new_map))] for i in range(len(new_map))] # 체스판위에 어떤 말들이 위치해 있는지 저장하기 위함
    for i in range(len(horse_info)): # 초기 말들의 위치를 체스판위에 올려놓음
        r, y = horse_info[i][0], horse_info[i][1]
        current_board[r][y].append(i)
    count = 0
    while count <= 1000:
        count += 1
        for horse in range(horse_count):
            cur_r, cur_y = horse_info[horse][0], horse_info[horse][1] # 소환하려는 말의 위치.
            new_r, new_y = horse_info[horse][0] + dr[horse_info[horse][2]], \
                           horse_info[horse][1] + dy[horse_info[horse][2]]  # 여기서 벽에 부딪힐때 체크해야됨 -> 맵을 파란색 보드로 둘러쌈으로써 문제해결

            if new_map[new_r][new_y] == 0: #가야할 곳이 흰색 땅일때
                to_white_board(current_board, cur_r, cur_y, new_r, new_y, horse, horse_info)
            elif new_map[new_r][new_y] == 1: #가야할 곳이 빨간색 땅일때
                to_red_board(current_board, cur_r, cur_y, new_r, new_y, horse, horse_info)
            elif new_map[new_r][new_y] == 2: # 가야할 곳이 파란색 땅일때
                change_direction(horse, horse_info) #반대 방향으로
                new_r, new_y = horse_info[horse][0] + dr[horse_info[horse][2]], \
                         horse_info[horse][1] + dy[horse_info[horse][2]]  # 방향 반대인 상태에서 새로운 좌표
                if new_map[new_r][new_y] == 0:
                    to_white_board(current_board, cur_r, cur_y, new_r, new_y, horse, horse_info)
                elif new_map[new_r][new_y] == 1:
                    to_red_board(current_board, cur_r, cur_y, new_r, new_y, horse, horse_info)

            # 게임이 끝나는지 체크
            if len(current_board[new_r][new_y]) > 3:
                return count

    return -1

def surround_blue_wall(map):
    n_map = map
    for row in n_map:
        row.insert(0, 2)
        row.append(2)
    x = len(n_map[0])
    nl = [2] * x
    n_map.insert(0, nl)
    n_map.append(nl)
    return n_map

def to_white_board(board, r, y, nr, ny, horse, horse_info):
    # 보드의 해당 위치에서 해당하는 말의 인덱스를 알아야 한다 -> 위에 쌓여진애들 같이 옮기기 위해서
    # print(horse)
    # print(board)
    # print('(r,y):',r,y)
    i = board[r][y].index(horse) # 이 말의 위치
    board[nr][ny].extend(board[r][y][i:]) # 이 말 위에 있는 애들을 한번에 새로운 보드위로 옮긴다.
    for hor in board[r][y][i:]: # 같이 업혀서 이동하는 말 덩어리 위치정보 갱신
        horse_info[hor][0], horse_info[hor][1] = nr, ny  # 말들의 위치 정보갱신
    board[r][y] = board[r][y][:i] # 기존 보드 위에서 말이 움직이고 난 후를 표현한다.


def to_red_board(board, r, y, nr, ny, horse, horse_info):
    i = board[r][y].index(horse)  # 이 말의 위치
    board[nr][ny].extend(board[r][y][i:][::-1])  # 이 말 위에 있는 애들을 한번에 새로운 보드위로 옮긴다.
    for hor in board[r][y][i:]: # 같이 업혀서 이동하는 말 덩어리 위치정보 갱신
        horse_info[hor][0], horse_info[hor][1] = nr, ny  # 말들의 위치 정보갱신
    board[r][y] = board[r][y][:i]  # 기존 보드 위에서 말이 움직이고 난 후를 표현한다.
    # horse_info[horse][0], horse_info[horse][1] = nr, ny # 말들의 위치 정보갱신

def change_direction(horse, horse_info):
    horse_direction = horse_info[horse][2]

    if horse_direction == 0:
        horse_info[horse][2] = 1
    elif horse_direction == 1:
        horse_info[horse][2] = 0
    elif horse_direction == 2:
        horse_info[horse][2] = 3
    elif horse_direction == 3:
        horse_info[horse][2] = 2   #말들의 방향을 반대로 한다.


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
#
start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))