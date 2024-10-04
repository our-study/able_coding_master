import sys

data = sys.stdin.read().splitlines()
N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

edges.sort(key=lambda x: x[2])

parent = list(range(N))
rank = [1] * N

total_cost = 0

for u, v, cost in edges:
    u -= 1  
    v -= 1  

    root_u = u
    while parent[root_u] != root_u:
        root_u = parent[root_u]

    root_v = v
    while parent[root_v] != root_v:
        root_v = parent[root_v]

    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1
        total_cost += cost

print(total_cost)
