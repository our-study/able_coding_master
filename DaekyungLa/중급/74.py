import sys
from collections import deque


data = sys.stdin.read().strip().split('\n')
N, M = map(int, data[0].strip().split())
grid = [list(row) for row in data[1:N+1]]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * M for _ in range(N)]


def bfs(x, y, grid, visited, directions):
    queue = deque([(x, y)])
    visited[x][y] = True
    cells = [(x, y)]
    color_count = {'A': 0, 'B': 0}
    while queue:
        cx, cy = queue.popleft()
        if grid[cx][cy] in color_count:
            color_count[grid[cx][cy]] += 1
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny))
                cells.append((nx, ny))
    return cells, color_count


for i in range(N):
    for j in range(M):
        if grid[i][j] != 'X' and not visited[i][j]:
            cells, color_count = bfs(i, j, grid, visited, directions)
            if color_count['A'] > color_count['B']:
                for cx, cy in cells:
                    if grid[cx][cy] == 'B':
                        grid[cx][cy] = 'O'
            else:
                for cx, cy in cells:
                    if grid[cx][cy] == 'A':
                        grid[cx][cy] = 'O'

red_count = sum(row.count('A') for row in grid)
blue_count = sum(row.count('B') for row in grid)

print(red_count, blue_count)
