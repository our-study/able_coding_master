import sys
from collections import deque

input = sys.stdin.read
data = input().strip().split()
target = int(data[0])
start = int(data[1])

if start >= target:
    print(start - target)
else:
    queue = deque([(start, 0)])  
    visited = set()
    visited.add(start)
    
    while queue:
        current, steps = queue.popleft()
        
        if current == target:
            print(steps)
            break
        if current + 1 not in visited and current + 1 <= 100000:
            queue.append((current + 1, steps + 1))
            visited.add(current + 1)
        
        if current - 1 not in visited and current - 1 >= 0:
            queue.append((current - 1, steps + 1))
            visited.add(current - 1)
        
        if current * 2 not in visited and current * 2 <= 100000:
            queue.append((current * 2, steps + 1))
            visited.add(current * 2)
