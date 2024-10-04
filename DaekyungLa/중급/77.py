import sys
from collections import defaultdict
from itertools import permutations


data = sys.stdin.read().strip().split('\n')
index = 0

# graph1
N1, M1 = map(int, data[index].split())
index += 1
graph1 = defaultdict(set)

for _ in range(M1):
    u, v = map(int, data[index].split())
    graph1[u].add(v)
    graph1[v].add(u)
    index += 1

# graph2
N2, M2 = map(int, data[index].split())
index += 1
graph2 = defaultdict(set)

for _ in range(M2):
    u, v = map(int, data[index].split())
    graph2[u].add(v)
    graph2[v].add(u)
    index += 1


def are_isomorphic(graph1, graph2, n):
    for perm in permutations(range(1, n + 1)):
        mapped_graph = defaultdict(set)
        for u in range(1, n + 1):
            for v in graph1[u]:
                mapped_graph[perm[u - 1]].add(perm[v - 1])
        if all(mapped_graph[u] == graph2[u] for u in range(1, n + 1)):
            return True
    return False

if N1 != N2 or M1 != M2:
    print("NO")
else:
    if are_isomorphic(graph1, graph2, N1):
        print("YES")
    else:
        print("NO")
