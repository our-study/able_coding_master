from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))

queue = deque(range(1, N+1))
rotation_count = 0

for target in targets:
    idx = queue.index(target)
    left_rotations = idx
    right_rotations = len(queue) - idx
    rotation_count += min(left_rotations, right_rotations)
    
    if left_rotations <= right_rotations:
        queue.rotate(-left_rotations)
    else:
        queue.rotate(right_rotations)
    queue.popleft()

print(rotation_count)
