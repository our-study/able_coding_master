import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
count = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = grid[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

for i in range(N):
    for j in range(M):
        for x in range(i, N):
            for y in range(j, M):
                total = prefix_sum[x+1][y+1] - prefix_sum[i][y+1] - prefix_sum[x+1][j] + prefix_sum[i][j]
                if total == 10:
                    count += 1

print(count)
