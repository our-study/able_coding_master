import sys

N = int(sys.stdin.readline())
initial_state = [list(map(int, input().strip())) for _ in range(5)]
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]

def next_generation(current_gen):
    next_gen = [[0] * 5 for _ in range(5)]  
    for r in range(5):
        for c in range(5):
            alive_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 5 and 0 <= nc < 5 and current_gen[nr][nc] == 1:
                    alive_neighbors += 1
            if current_gen[r][c] == 1:  
                if alive_neighbors == 2 or alive_neighbors == 3:
                    next_gen[r][c] = 1  
                else:
                    next_gen[r][c] = 0  
            else:  
                if alive_neighbors == 3:
                    next_gen[r][c] = 1  
                else:
                    next_gen[r][c] = 0  
    return next_gen
    
current_state = initial_state
for _ in range(N):
    current_state = next_generation(current_state)

for row in current_state:
    print(''.join(map(str, row)))
