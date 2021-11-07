current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    # r:북쪽으로부터떨어진 칸의 개수, c: 서쪽으로부터, d: 0,1,2,3 북 동 남 서
    dx, dy, cur_head = c, r, d
    clean_count = 1
    dx_move = [0, 1, 0, -1]
    dy_move = [-1, 0, 1, 0]
    room_map[dy][dx] = 2  # 현재위치를 청소한다
    # print('처음 청소하였씁니다 dx:', dx, 'dy:', dy)
    rotate = 4
    while rotate: ## 위의 두 코드 로봇이 언제까지 움직일 것인가에 대해 그냥 대충
        rotate -= 1 ## 이 방식 확실치 않음  ->>> 맞는 방식인것같다!!

        cur_head = (cur_head + 3) % 4 # 헤드는 무조건 돌아감'

        dx_cur = dx + dx_move[cur_head]
        dy_cur = dy + dy_move[cur_head]
        if room_map[dy_cur][dx_cur] == 0: # 위의 세줄, 헤드가 바라보는 위치가 빈공간인지 아닌지를 체크하는 코드
            dx, dy = dx_cur, dy_cur #빈공간인지를 확인하면 그쪽으로 이동하기
            room_map[dy][dx] = 2  # 청소를 하기
            # print('남은 회전수:', rotate, '청소하였씁니다 dx:', dx, 'dy:', dy)
            clean_count += 1 #청소 횟수 증가
            rotate = 4 # 반복동작 다시 시작
            # print('반복동작 초기화1:',rotate)

        if rotate == 0: #청소 한것없이 4회의 회전이 끝났을 시에
            dx_back, dy_back = dx - dx_move[cur_head], dy - dy_move[cur_head]
            if room_map[dy_back][dx_back] == 1: #백무빙의 방향에 벽일시에
                break # 반복문 탈출
            else: #백무빙의 방향에 벽이 아닐시
                dx, dy = dx_back, dy_back  # 백무빙한다.
                rotate = 4  # 4회전 반복동작 다시 시작
                # print('반복동작 초기화2:', rotate)

    return clean_count
# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))

current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))