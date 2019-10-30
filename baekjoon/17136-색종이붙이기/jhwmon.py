'''
주어진 예제는 모두 맞고, 시간도 문제 없어보이는데
문제 제출하면 20% 조금 넘어가면서 실패 나옴

원인을 모르겠음.... 나중에 다시 고민
'''

import copy

square = []
cnt = 0     # 총 덮은 종이의 개수
ncnt = 5    # 색종이 개수
flag = 0

for i in range(0, 10):
    square.append(list(map(int, list(input().split()))))

# 5 ~ 1 종이 찾기 반복
for n in reversed(range(1, 6)):
    ncnt = 5
    if cnt == -1:
        break
    # 모든 칸을 반복 순회
    for y in range(10):
        if ncnt < 0 or cnt == -1:
            cnt = -1
            break

        for x in range(10):
            # 1이 아닌 값은 패스
            if square[y][x] != 1:
                continue
            else:
                # n x n 모두 1인지 확인 1이면?
                tmp_square = copy.deepcopy(square)

                flag = 1

                for a in range(0, n):
                    if flag == 0 or y+a >= 10:
                        break

                    for b in range(0, n):
                        if flag == 0 or x+b >= 10:
                            break

                        if tmp_square[y+a][x+b] == 1:
                            tmp_square[y+a][x+b] = 0
                        else:
                            flag = 0

                # n x n 색종이 사용
                if flag == 1:
                    flag = 0
                    cnt += 1
                    ncnt -= 1
                    square = tmp_square

print(cnt)