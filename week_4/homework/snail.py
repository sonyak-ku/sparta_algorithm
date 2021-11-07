## n 이란 숫자를 제시하면, 한변이 n 인 정사각형을 그린뒤에, 달팽이처럼 시계 방향으로 계속 감아서 회전하고,
## 마지막에는 위에서부터 한변씩 리스트로 한번에 숫자를 연결해서 제시

def snail(n):
    snail_list = [[0 for j in range(n)] for i in range(n)]
    #동0, 남1, 서2, 북3
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cur_x = 0
    cur_y = 0
    head = 0
    count = 1
    k = n*n
    while(k):
        k = k-1 # 한턴 사용
        snail_list[cur_y][cur_x] = count #현재 위치에 값 넣기
        count = count + 1  ## 넣을 값 증가


        if cur_x + dx[head] > n - 1 or cur_x + dx[head] < 0 or cur_y + dy[head] > n - 1 or cur_y + dy[head] < 0 or snail_list[cur_y + dy[head]][cur_x + dx[head]] != 0: # 벽을 만났을 때, 이미 지정된 값일 때
            head = (head + 1) % 4 # 방향 수정하고 코드짜기
            cur_x = cur_x + dx[head]
            cur_y = cur_y + dy[head]
        else: # 벽 전
            cur_x = cur_x + dx[head]
            cur_y = cur_y + dy[head]

    complist = [item for list in snail_list for item in list] # 이중for 문은 리스트 한줄로 뽑아내는 코드
    return complist

print(snail(5))
