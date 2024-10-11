from itertools import combinations
from collections import deque
import copy

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 재규어 확산
def bfs(spread_map, n, m):
    queue = deque()
    
    # 재규어가 있는 위치를 모두 큐에 넣기
    for i in range(n):
        for j in range(m):
            if spread_map[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        
        # 재규어가 상하좌우로 확산
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 유효한 범위 내에서 빈 칸일 경우 확산
            if 0 <= nx < n and 0 <= ny < m and spread_map[nx][ny] == 0:
                spread_map[nx][ny] = 2
                queue.append((nx, ny))

# 안전한 구역의 개수를 세는 함수
def count_safe_area(spread_map, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if spread_map[i][j] == 0:  # 빈 칸일 경우 안전한 구역
                count += 1
    return count

# 입력 받기
n, m = map(int, input().split())
zoo = [list(map(int, input().split())) for _ in range(n)]

# 빈 칸 좌표 수집
empty_spaces = [(i, j) for i in range(n) for j in range(m) if zoo[i][j] == 0]

# 3개의 울타리를 세울 수 있는 모든 경우의 수
wall_combinations = list(combinations(empty_spaces, 3))

max_safe_area = 0

# 모든 울타리 설치 경우에 대해 확인
for walls in wall_combinations:
    # 동물원 상태를 복사
    temp_zoo = copy.deepcopy(zoo)
    
    # 울타리 설치
    for wx, wy in walls:
        temp_zoo[wx][wy] = 1
    
    # 재규어 확산
    bfs(temp_zoo, n, m)
    
    # 안전 구역 계산
    safe_area = count_safe_area(temp_zoo, n, m)
    
    # 최대 안전 구역 갱신
    max_safe_area = max(max_safe_area, safe_area)

# 결과 출력
print(max_safe_area)
