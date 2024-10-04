def is_tetromino(grid): 
    # 테트로미노의 '#' 개수 세기 
    count = 0 
    for row in grid: 
        count += row.count('#') 
     
    # '#'의 개수가 4개가 아니면 NO 
    if count != 4: 
        return \"NO\" 
     
    # 시작점 찾기 
    start = None 
    for i in range(5): 
        for j in range(5): 
            if grid[i][j] == '#': 
                start = (i, j) 
                break 
        if start: 
            break 
     
    # DFS로 연결된 '#' 세기 
    stack = [start] 
    visited = set() 
    visited.add(start) 
     
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 
     
    while stack: 
        x, y = stack.pop() 
        for dx, dy in directions: 
            nx, ny = x + dx, y + dy 
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visited and grid[nx][ny] == '#': 
                visited.add((nx, ny)) 
                stack.append((nx, ny)) 
     
    # 방문한 '#'의 개수가 4인지 확인 
    if len(visited) == 4: 
        return \"YES\" 
    else: 
        return \"NO\" 
 
# 입력 받기 
grid = [input().strip() for _ in range(5)] 
 
# 결과 출력 
result = is_tetromino(grid) 
print(result) 
