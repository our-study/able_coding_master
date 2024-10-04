from collections import deque 
 
# 상하좌우 탐색을 위한 방향 벡터 
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 
 
# BFS 탐색 함수 
def bfs(grid, visited, start, target): 
    queue = deque([start]) 
    visited[start[0]][start[1]] = True 
    component = [start] 
     
    while queue: 
        x, y = queue.popleft() 
         
        for i in range(4): 
            nx, ny = x + dx[i], y + dy[i] 
            if 0 <= nx < 10 and 0 <= ny < 20 and not visited[nx][ny] and grid[nx][ny] == target: 
                visited[nx][ny] = True 
                queue.append((nx, ny)) 
                component.append((nx, ny)) 
     
    return component 
 
# 첫 번째 조건을 확인하는 함수: 모든 '.'이 연결되어 있는지 확인 
def check_all_dots_connected(grid): 
    visited = [[False] * 20 for _ in range(10)] 
     
    # 첫 '.'을 찾는다. 
    for i in range(10): 
        for j in range(20): 
            if grid[i][j] == '.': 
                # 첫 '.'에서 BFS로 모든 '.'을 탐색 
                all_dots = bfs(grid, visited, (i, j), '.') 
                # 모든 '.'이 방문되었는지 확인 
                for x in range(10): 
                    for y in range(20): 
                        if grid[x][y] == '.' and not visited[x][y]: 
                            return False 
                return True 
    return False 
 
# 두 번째 조건을 확인하는 함수: 6칸 이상의 '#' 덩어리가 '.'으로 둘러싸여 있는지 확인 
def check_surrounded_walls(grid): 
    visited = [[False] * 20 for _ in range(10)] 
     
    for i in range(10): 
        for j in range(20): 
            if grid[i][j] == '#' and not visited[i][j]: 
                wall_component = bfs(grid, visited, (i, j), '#') 
                if len(wall_component) >= 6: 
                    # '#' 덩어리가 모두 '.'으로 둘러싸여 있는지 확인 
                    surrounded = True 
                    for x, y in wall_component: 
                        for k in range(4): 
                            nx, ny = x + dx[k], y + dy[k] 
                            if 0 <= nx < 10 and 0 <= ny < 20 and grid[nx][ny] == '#': 
                                continue 
                            if not (0 <= nx < 10 and 0 <= ny < 20 and grid[nx][ny] == '.'): 
                                surrounded = False 
                                break 
                        if not surrounded: 
                            break 
                    if surrounded: 
                        return True 
    return False 
 
# 입력 및 처리 
N = int(input())  # 도면의 수 
 
for _ in range(N): 
    grid = [input().strip() for _ in range(10)] 
     
    condition1 = check_all_dots_connected(grid) 
    condition2 = check_surrounded_walls(grid) 
     
    if condition1 and condition2: 
        print(3) 
    elif condition1: 
        print(1) 
    elif condition2: 
        print(2) 
    else: 
        print(0)
