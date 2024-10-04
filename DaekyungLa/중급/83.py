import sys
from collections import deque

puzzle = [input().strip() for _ in range(2)]
start = ''.join(puzzle)
goal = '123X'
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start):
    queue = deque([(start, start.index('X'), 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        current, empty_index, steps = queue.popleft()
        if current == goal:
            return steps
        empty_row, empty_col = divmod(empty_index, 2)
        for move in moves:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            if 0 <= new_row < 2 and 0 <= new_col < 2:
                new_index = new_row * 2 + new_col
                new_state = list(current)
                new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, new_index, steps + 1))
    return -1

result = bfs(start)
print(result)
