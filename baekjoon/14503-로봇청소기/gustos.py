# 오답: 이유 못 찾음...
N, M = map(int, input().split())

r, c, d = map(int, input().split())

pos = list() # 현 방향의 왼쪽 포지션 체크

pos.append((0, -1)) # 서쪽으로
pos.append((-1, 0)) # 북쪽으로
pos.append((0, 1)) # 동쪽으로
pos.append((1, 0)) # 남쪽으로

answer = 0

cleaning_map = [[0] * M for _ in range(N)]
is_clean = True # 청소 했나

for row in range(N):
    temp = input().split()
    for col in range(M):
        cleaning_map[row][col] = int(temp[col])

while(True):
    # 해당 자리 청소
    if is_clean:
        cleaning_map[r][c] = 2
        answer += 1

    temp_d = (d + 3) % 4 # 방향 전환

    # 다음 위치 값 계산
    temp_r = r + pos[temp_d][0]
    temp_c = c + pos[temp_d][1]
    temp_pos = cleaning_map[temp_r][temp_c]

    # 왼쪽 방향 청소 가능
    if temp_pos == 0:
        r = temp_r
        c = temp_c
        d = temp_d
        is_clean = True
        continue
    # 왼쪽 방향 청소 불가능
    else:
        is_clean = False

        # 청소 가능 구역이 없을 경우
        if cleaning_map[r - 1][c] != 0 and cleaning_map[r][c - 1] != 0 and cleaning_map[r + 1][c] != 0 and cleaning_map[r][c + 1] != 0:

            # 후진 방향 계산
            temp_d = (d + 2) % 4

            # 후진
            r = r + pos[temp_d][0]
            c = c + pos[temp_d][1]

            # 후진이 불가능한 경우
            if cleaning_map[r][c] == 1:
                break

        else:
            d = temp_d

print(answer)

