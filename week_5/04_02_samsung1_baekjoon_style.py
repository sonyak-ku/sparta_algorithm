import copy

# 동 서 북 남
# →, ←, ↑, ↓
# 맵의 번호가 1.1 로 시작한다는게 주위를 벽으로 둘러 쌓아도 괜찮다는 뜻처럼 여겨지네용
dr = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n_map = copy.deepcopy(game_map)
    new_map = surround_blue_wall(n_map) #-> 이중리스트 완전복사를 하여 같은 메모리를 공유해서 맵이 변하는 문제를 해결
    horse_info = horse_location_and_directions
    for i in horse_location_and_directions: # 맵을 둘러 쌓았기 때문에 생기는 위치 변화 체크
        i[2] -= 1 # 방향을 0,1,2,3 으로 사용하기 위해

    current_board = [[[] for j in range(len(new_map))] for i in range(len(new_map))] # 체스판위에 어떤 말들이 위치해 있는지 저장하기 위함
    for i in range(len(horse_info)): # 초기 말들의 위치를 체스판위에 올려놓음
        r, y = horse_info[i][0], horse_info[i][1]
        current_board[r][y].append(i)
    count = 0
    # print('처음 체스판', current_board)
    while count < 1000:
        count += 1
        for horse in range(horse_count):
            cur_r, cur_y = horse_info[horse][0], horse_info[horse][1] # 소환하려는 말의 위치.
            # print('cur',cur_r, cur_y)
            new_r, new_y = horse_info[horse][0] + dr[horse_info[horse][2]], \
                           horse_info[horse][1] + dy[horse_info[horse][2]]  # 여기서 벽에 부딪힐때 체크해야됨 -> 맵을 파란색 보드로 둘러쌈으로써 문제해결
            # print('new', new_r, new_y)
            if new_map[new_r][new_y] == 0: #가야할 곳이 흰색 땅일때
                # print('흰색땅으로')
                to_white_board(current_board, cur_r, cur_y, new_r, new_y, horse, horse_info)
            elif new_map[new_r][new_y] == 1: #가야할 곳이 빨간색 땅일때
                # print('빨간땅으로')
                to_red_board(current_board, cur_r, cur_y, new_r, new_y, horse, horse_info)
            elif new_map[new_r][new_y] == 2: # 가야할 곳이 파란색 땅일때
                # print('파란땅으로', new_r, new_y)
                change_direction(horse, horse_info) #반대 방향으로
                new_r, new_y = horse_info[horse][0] + dr[horse_info[horse][2]], \
                         horse_info[horse][1] + dy[horse_info[horse][2]]  # 방향 반대인 상태에서 새로운 좌표
                if new_map[new_r][new_y] == 0:
                    to_white_board(current_board, cur_r, cur_y, new_r, new_y, horse, horse_info)
                elif new_map[new_r][new_y] == 1:
                    to_red_board(current_board, cur_r, cur_y, new_r, new_y, horse, horse_info)

            # print(current_board)
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

def change_direction(horse, horse_info):
    # print('방향변화', horse, horse_info)
    horse_direction = horse_info[horse][2]
    if horse_direction == 0:
        horse_info[horse][2] = 1
    elif horse_direction == 1:
        horse_info[horse][2] = 0
    elif horse_direction == 2:
        horse_info[horse][2] = 3
    elif horse_direction == 3:
        horse_info[horse][2] = 2   #말들의 방향을 반대로 한다.

n, k = map(int, input().split()) # 체스판 크기 n*n, 말의 개수 k

chess_map = [list(map(int, input().split())) for r in range(n)]
horse_info = [list(map(int, input().split())) for r in range(k)]

# print(chess_map)
# print(horse_info)
print(get_game_over_turn_count(k, chess_map, horse_info))