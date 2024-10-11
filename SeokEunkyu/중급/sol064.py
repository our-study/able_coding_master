import sys 
import sys 
sys.setrecursionlimit(1000000) 
 
def input(): 
    return sys.stdin.readline() 
 
def dfs(x, y, N, M, grid, visited, region_cells): 
    stack = [(x, y)] 
    visited[x][y] = True 
    region_cells.append((x, y)) 
     
    # 상, 하, 좌, 우 방향 
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 
     
    while stack: 
        cx, cy = stack.pop() 
        for dx, dy in directions: 
            nx, ny = cx + dx, cy + dy 
            if 0 <= nx < N and 0 <= ny < M: 
                if not visited[nx][ny] and grid[nx][ny] != 'X': 
                    visited[nx][ny] = True 
                    stack.append((nx, ny)) 
                    region_cells.append((nx, ny)) 
 
def process_regions(N, M, grid): 
    visited = [[False for _ in range(M)] for _ in range(N)] 
    for i in range(N): 
        for j in range(M): 
            if not visited[i][j] and grid[i][j] != 'X': 
                region_cells = [] 
                dfs(i, j, N, M, grid, visited, region_cells) 
                # Count A and B in the region 
                count_A = 0 
                count_B = 0 
                for x, y in region_cells: 
                    if grid[x][y] == 'A': 
                        count_A += 1 
                    elif grid[x][y] == 'B': 
                        count_B += 1 
                # Apply modification rules 
                if count_A > count_B: 
                    # Delete all B's 
                    for x, y in region_cells: 
                        if grid[x][y] == 'B': 
                            grid[x][y] = 'O' 
                else: 
                    # Delete all A's 
                    for x, y in region_cells: 
                        if grid[x][y] == 'A': 
                            grid[x][y] = 'O' 
    # After processing all regions, count remaining A's and B's 
    total_A = 0 
    total_B = 0 
    for i in range(N): 
        for j in range(M): 
            if grid[i][j] == 'A': 
                total_A += 1 
            elif grid[i][j] == 'B': 
                total_B += 1 
    return total_A, total_B 
 
if __name__ == \"__main__\": 
    import sys 
    input = sys.stdin.read 
    data = input().split() 
     
    # Read N and M 
    N = int(data[0]) 
    M = int(data[1]) 
     
    # Read grid 
    grid = [] 
    idx = 2 
    for _ in range(N): 
        row = list(data[idx]) 
        grid.append(row) 
        idx +=1 
     
    # Process regions 
    remaining_A, remaining_B = process_regions(N, M, grid) 
     
    # Output 
    print(remaining_A, remaining_B) 
