import sys 
import heapq 
 
def dijkstra(graph, start, end): 
    N = len(graph) 
    distances = [-1] * (N + 1) 
    distances[start] = float('inf')  # 시작점은 무한대 
    pq = [(-float('inf'), start)]  # (현재까지의 최대 시간, 노드) 
     
    while pq: 
        current_max_time, current_node = heapq.heappop(pq) 
        current_max_time = -current_max_time 
         
        if current_node == end: 
            return current_max_time 
         
        for neighbor, time in graph[current_node]: 
            max_time_through_neighbor = min(current_max_time, time) 
            if distances[neighbor] < max_time_through_neighbor: 
                distances[neighbor] = max_time_through_neighbor 
                heapq.heappush(pq, (-max_time_through_neighbor, neighbor)) 
     
    return -1  # 도달할 수 없는 경우 
 
def main(): 
    input = sys.stdin.read 
    data = input().splitlines() 
     
    first_line = list(map(int, data[0].split())) 
    N = first_line[0] 
    M = first_line[1] 
     
    graph = [[] for _ in range(N + 1)] 
     
    for i in range(1, M + 1): 
        A, B, C = map(int, data[i].split()) 
        graph[A].append((B, C)) 
        graph[B].append((A, C)) 
     
    start, end = map(int, data[M + 1].split()) 
     
    result = dijkstra(graph, start, end) 
    print(result) 
 
if __name__ == \"__main__\": 
    main() 
