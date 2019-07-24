import sys

# 0,0 은 각 블럭 모양의 첫 시작점을 기준으로
BLOCK = [
    [[0, 0], [0, 1], [1, 1]], # ⏋
    [[0, 0], [1, 0], [0, 1]], # ⎾
    [[0, 0], [1, 0], [1, 1]], # ⎿
    [[0, 0], [1, 0], [1, -1]], # ⏌
]

# x = 0일때는 1, 4 블록 제외
# x = W일때는 2, 3 블록 제외
# y = W일때는 비교할 필요 없음

in1 = sys.stdin.readline()
in2 = sys.stdin.readline()
C = int(in1)
H, W = list(map(int, in2.split(' ')))

BOARD = [[0]*W for _ in range(H)]
for c in range(0, C):
    for h in range(0, H):
        row = sys.stdin.readline()
        for w in range(0, W):
            if row[w] == '#':
                BOARD[h][w] = 1



def cover_board(BOARD, row_idx, col_idx):
    global BLOCK
    global H, W
    if row_idx == H-1:
        continue
    elif col_idx == W-1
