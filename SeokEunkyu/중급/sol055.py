from collections import deque

def bfs(start, goal):
    # 방문 여부 체크 배열 (최대 100,000까지)
    visited = [False] * 100001
    
    # 큐 생성 (현재 숫자와 연산 횟수 저장)
    queue = deque([(start, 0)])
    
    # BFS 시작
    while queue:
        current, count = queue.popleft()
        
        # 목표 숫자에 도달한 경우
        if current == goal:
            return count
        
        # 각 경우에 대해 탐색 (+1, -1, *2)
        for next_num in (current + 1, current - 1, current * 2):
            if 0 <= next_num <= 100000 and not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, count + 1))

# 입력 받기
n, k = map(int, input().split())

# 결과 출력
print(bfs(k, n))
