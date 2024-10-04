
import sys
import heapq

input = sys.stdin.read
data = input().strip().split()
N = int(data[0])

stores = []
index = 1
for i in range(N):
    a = int(data[index])
    b = int(data[index + 1])
    stores.append((a, b))
    index += 2

L = int(data[index])
P = int(data[index + 1])

stores.sort()


max_heap = []
stops = 0
i = 0

while P < L:
    while i < N and stores[i][0] <= P:
        heapq.heappush(max_heap, -stores[i][1])
        i += 1
    if not max_heap:
        stops = -1
        break.
    P += -heapq.heappop(max_heap)
    stops += 1
print(stops)
