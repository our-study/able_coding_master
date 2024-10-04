import sys 
import itertools 
 
def read_input(): 
    \"\"\" 
    표준 입력에서 데이터를 읽어 N, M과 그리드를 반환합니다. 
    \"\"\" 
    input = sys.stdin.read().split() 
    N = int(input[0]) 
    M = int(input[1]) 
    grid = [] 
    idx = 2 
    for _ in range(N): 
        row = list(map(int, input[idx:idx+M])) 
        grid.append(row) 
        idx += M 
    return N, M, grid 
 
def generate_boomerangs(N, M, grid): 
    \"\"\" 
    가능한 모든 부메랑을 생성하고, 각 부메랑의 셀과 강도를 리스트로 반환합니다. 
    \"\"\" 
    boomerangs = [] 
    # 각 셀을 중심으로 4가지 방향의 부메랑을 시도 
    for i in range(N): 
        for j in range(M): 
            # 4가지 방향: 오른쪽 아래, 왼쪽 아래, 오른쪽 위, 왼쪽 위 
            directions = [ 
                [(i, j), (i, j+1), (i+1, j)],    # 오른쪽 아래 
                [(i, j), (i, j-1), (i+1, j)],    # 왼쪽 아래 
                [(i, j), (i, j+1), (i-1, j)],    # 오른쪽 위 
                [(i, j), (i, j-1), (i-1, j)]     # 왼쪽 위 
            ] 
            for dir in directions: 
                valid = True 
                cells = [] 
                for x, y in dir: 
                    if 0 <= x < N and 0 <= y < M: 
                        cells.append((x, y)) 
                    else: 
                        valid = False 
                        break 
                if valid: 
                    # 중심 셀은 dir[0] 
                    center = dir[0] 
                    strength = grid[center[0]][center[1]] * 2 
                    strength += grid[dir[1][0]][dir[1][1]] 
                    strength += grid[dir[2][0]][dir[2][1]] 
                    # Convert cell positions to unique indices 
                    cell_indices = [c[0]*M + c[1] for c in cells] 
                    boomerangs.append( (cell_indices, strength) ) 
    return boomerangs 
 
def backtrack(boomerangs, index, used, current_sum, max_sum): 
    \"\"\" 
    백트래킹을 통해 부메랑을 선택하여 최대 합을 찾습니다. 
     
    Parameters: 
    - boomerangs: 리스트 of tuples (cell_indices, strength) 
    - index: 현재 부메랑 인덱스 
    - used: set of used cell indices 
    - current_sum: 현재까지의 합 
    - max_sum: 현재까지의 최대 합 
    \"\"\" 
    if index == len(boomerangs): 
        return max(current_sum, max_sum) 
     
    # 현재 부메랑을 선택하지 않는 경우 
    max_sum = backtrack(boomerangs, index + 1, used, current_sum, max_sum) 
     
    # 현재 부메랑을 선택하는 경우 
    cells, strength = boomerangs[index] 
    overlap = False 
    for cell in cells: 
        if cell in used: 
            overlap = True 
            break 
    if not overlap: 
        # 선택 가능한 경우 
        for cell in cells: 
            used.add(cell) 
        max_sum = backtrack(boomerangs, index + 1, used, current_sum + strength, max_sum) 
        for cell in cells: 
            used.remove(cell) 
     
    return max_sum 
 
def main(): 
    N, M, grid = read_input() 
    boomerangs = generate_boomerangs(N, M, grid) 
    # 정렬: 강도가 큰 부메랑부터 시도 (최적화) 
    boomerangs.sort(key=lambda x: x[1], reverse=True) 
    max_sum = backtrack(boomerangs, 0, set(), 0, 0) 
    print(max_sum) 
 
if __name__ == \"__main__\": 
    main() 
