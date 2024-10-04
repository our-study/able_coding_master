import sys

N = int(sys.stdin.readline().strip())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

min_white = float('inf')

for row_mask in range(1 << N):
    temp_board = [[board[i][j] for j in range(N)] for i in range(N)]

    for i in range(N):
        if row_mask & (1 << i):  
            for j in range(N):
                temp_board[i][j] = 'B' if temp_board[i][j] == 'W' else 'W'

    for j in range(N):
        count_w = sum(1 for i in range(N) if temp_board[i][j] == 'W')
        if count_w > N // 2:  
            for i in range(N):
                temp_board[i][j] = 'B' if temp_board[i][j] == 'W' else 'W'

    total_white = sum(1 for i in range(N) for j in range(N) if temp_board[i][j] == 'W')
    min_white = min(min_white, total_white)

print(min_white)
