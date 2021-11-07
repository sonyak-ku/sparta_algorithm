# k = 4  # 말의 개수
#
# chess_map = [
#     [0, 0, 2, 0],
#     [0, 0, 1, 0],
#     [0, 0, 1, 2],
#     [0, 2, 0, 0]
# ]
# start_horse_location_and_directions = [
#     [1, 0, 0],
#     [2, 1, 2],
#     [1, 1, 0],
#     [3, 0, 1]
# ]
# # 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!

k = 4  # 말의 개수
# 흰, 빨(쌓을때 방향 뒤집어서 쌓기), 파(벽 이라고 생각-반대방향으로 한칸)
# 0,   1                      2

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


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions): #말의 개수, 체스판 정보, 현재 말의 위치와 방향
    map_stack = [[[] for j in range(len(game_map))] for i in range(len(game_map))] # 말의 위치를 저장할 공간
    #체스판에 말들을 배치하기 (스택의 형식으로)
    for i in range(horse_count):
        x, y = horse_location_and_directions[i][0], horse_location_and_directions[i][1]  # k번째 말의 현재 위치를 확인
        map_stack[x][y].append(i)
    turn_count = 0
    while turn_count <= 1000:
        turn_count += 1
        for k in range(horse_count): #말을 0 번부터 k-1 번까지의 k개로 두고 : 요구하는 바는 1번 부터 k번까지의 k개
            x, y = horse_location_and_directions[k][0], horse_location_and_directions[k][1] # k번째 말의 현재 위치를 확인
            move_direction = horse_location_and_directions[k][2]
            new_x = x + dr[move_direction]
            new_y = y + dy[move_direction] # 이동하려는 칸 의 좌표 nx, ny
            # 이동하려는 칸이 벽을 만났을때


            # A번 말이 이동하려는 칸이
            # 말의 이동 - 보드판위의 체스말의 위치 갱신/ 체스 자체의 위치 정보 갱신
            board_color = game_map[new_x][new_y]
            if board_color == 0: # 흰색일 경우
                cur = map_stack[x][y].index(k) # 현재 보드판 위의 k번째 말의 위치
                stack = map_stack[x][y][cur:] # k 번째 말의 덩어리를 꺼냄
                map_stack[x][y] = map_stack[x][y][:cur] # k 번째 말의 덩어리를 꺼내면서 보드 판 위의 체스말위치 갱신
                map_stack[new_x][new_y].extend(stack) # k 번째 덩어리를 순서대로 집어넣는다 (iter 형태)/ 보드 판 위의 체스말 위치 갱신
                horse_location_and_directions[k][0], horse_location_and_directions[k][1] = new_x, new_y # 체스 자체의 위치 정보 갱신
            elif board_color == 1: # 빨간색일 경우
                cur = map_stack[x][y].index(k)
                stack = map_stack[x][y][cur:]
                map_stack[x][y] = map_stack[x][y][:cur]
                map_stack[new_x][new_y].extend(stack[::-1])  # k 번째 덩어리를 ===반대=== 순서대로 집어넣는다
                horse_location_and_directions[k][0], horse_location_and_directions[k][1] = new_x, new_y
            elif board_color == 2: # 파란색의 경우
                pass




    return -1 #게임이 1000회의 반복이내에 끝나지 않은 경우


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

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