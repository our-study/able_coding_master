import sys 
import heapq 
 
def min_rice_cakes(N, grid): 
    # 방향 벡터: 상, 하, 좌, 우 
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 
     
    # 2차원 배열로 최소 비용 저장, 초기값은 무한대로 설정 
    INF = float('inf') 
    dist = [[INF for _ in range(N)] for _ in range(N)] 
     
    # 시작점의 비용 설정 
    dist[0][0] = grid[0][0] 
     
    # 우선순위 큐 초기화: (누적 비용, 행, 열) 
    heap = [] 
    heapq.heappush(heap, (dist[0][0], 0, 0)) 
     
    while heap: 
        current_cost, x, y = heapq.heappop(heap) 
         
        # 목표 지점에 도달하면 비용 반환 
        if x == N-1 and y == N-1: 
            return current_cost 
         
        # 이미 더 낮은 비용으로 방문한 경우 무시 
        if current_cost > dist[x][y]: 
            continue 
         
        # 4방향으로 이동 시도 
        for dx, dy in directions: 
            nx, ny = x + dx, y + dy 
            # 경계 조건 확인 
            if 0 <= nx < N and 0 <= ny < N: 
                new_cost = current_cost + grid[nx][ny] 
                if new_cost < dist[nx][ny]: 
                    dist[nx][ny] = new_cost 
                    heapq.heappush(heap, (new_cost, nx, ny)) 
     
    # 목표 지점에 도달할 수 없는 경우 (문제 조건 상 항상 가능하므로 이 경우는 없음) 
    return -1 
 
# 입력 받기 
if __name__ == \"__main__\": 
    import sys 
    input = sys.stdin.read 
    data = input().split() 
     
    N = int(data[0]) 
    grid = [] 
    idx = 1 
    for _ in range(N): 
        row = list(map(int, data[idx:idx+N])) 
        grid.append(row) 
        idx += N 
     
    result = min_rice_cakes(N, grid) 
    print(result) 
