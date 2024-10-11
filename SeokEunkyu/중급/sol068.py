# 인접한 8칸을 나타내는 방향 벡터
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

# 주어진 위치의 인접한 살아있는 세포 수를 계산하는 함수
def count_live_neighbors(board, x, y):
    live_neighbors = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:  # 격자판 내부의 유효한 위치인지 확인
            if board[nx][ny] == 1:
                live_neighbors += 1
    return live_neighbors

# 다음 세대를 계산하는 함수
def next_generation(board):
    new_board = [[0] * 5 for _ in range(5)]  # 다음 세대를 저장할 새로운 보드
    
    for i in range(5):
        for j in range(5):
            live_neighbors = count_live_neighbors(board, i, j)
            
            if board[i][j] == 1:  # 현재 세포가 살아있는 경우
                if live_neighbors == 2 or live_neighbors == 3:
                    new_board[i][j] = 1  # 생존
                else:
                    new_board[i][j] = 0  # 사망
            else:  # 현재 세포가 죽어있는 경우
                if live_neighbors == 3:
                    new_board[i][j] = 1  # 부활
                else:
                    new_board[i][j] = 0  # 여전히 사망
    
    return new_board

# 입력 받기
N = int(input())  # 세대 수
board = [list(map(int, list(input().strip()))) for _ in range(5)]

# N 세대 동안 변화를 시뮬레이션
for _ in range(N):
    board = next_generation(board)

# 결과 출력
for row in board:
    print(''.join(map(str, row)))
