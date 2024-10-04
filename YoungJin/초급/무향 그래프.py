import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dp = [[float('inf')] * N for _ in range(N)]
dp[0][0] = graph[0][0]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(N, graph, dp):
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = dp[x][y] + graph[nx][ny]
                if new_cost < dp[nx][ny]:
                    dp[nx][ny] = new_cost
                    queue.append((nx, ny))
    return dp[N - 1][N - 1]


print(bfs(N, graph, dp))