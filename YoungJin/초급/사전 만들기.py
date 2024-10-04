import sys

# 입력
n, m = map(int, sys.stdin.readline().strip().split(" "))

# 인접 행렬 초기화 (모든 값을 0으로 설정)
matrix = [[0] * (n + 1) for _ in range(n + 1)]

# 간선 정보 입력 및 처리
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 무향 그래프이므로 양방향 연결
    matrix[a][b] = 1
    matrix[b][a] = 1

# 출력
for row in matrix[1:]:
    for col in row[1:]:
        print(col, end=" ")
    print()

