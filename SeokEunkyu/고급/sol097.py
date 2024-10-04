from collections import deque 
 
def is_bipartite(graph, V): 
    colors = [-1] * (V + 1)  # -1: 미방문, 0: 집합 1, 1: 집합 2 
 
    for start in range(1, V + 1): 
        if colors[start] == -1:  # 방문하지 않은 노드 
            queue = deque([start]) 
            colors[start] = 0  # 첫 번째 집합에 색칠 
             
            while queue: 
                node = queue.popleft() 
                 
                for neighbor in graph[node]: 
                    if colors[neighbor] == -1:  # 방문하지 않은 노드 
                        colors[neighbor] = 1 - colors[node]  # 다른 집합에 색칠 
                        queue.append(neighbor) 
                    elif colors[neighbor] == colors[node]:  # 같은 집합 
                        return 0  # 이분 그래프가 아님 
 
    return 1  # 이분 그래프 
 
def main(): 
    import sys 
    input = sys.stdin.read 
    data = input().splitlines() 
     
    first_line = list(map(int, data[0].split())) 
    V = first_line[0]  # 죄수의 수 
    E = first_line[1]  # 친한 죄수 쌍의 수 
     
    graph = [[] for _ in range(V + 1)] 
 
    for i in range(1, E + 1): 
        a, b = map(int, data[i].split()) 
        graph[a].append(b) 
        graph[b].append(a) 
 
    result = is_bipartite(graph, V) 
    print(result) 
 
if __name__ == \"__main__\": 
    main() 
