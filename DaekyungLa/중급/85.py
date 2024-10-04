import sys

N = int(sys.stdin.readline().strip())
x1, y1 = map(int, sys.stdin.readline().strip().split())
x2, y2 = map(int, sys.stdin.readline().strip().split())

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, steps, visited):
    if steps == N:
        return 1 if (x, y) == (x2, y2) else 0
    
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            count += dfs(nx, ny, steps + 1, visited)
            visited.remove((nx, ny))  
    return count

visited = set()
visited.add((x1, y1))


result = dfs(x1, y1, 0, visited)
print(result)
