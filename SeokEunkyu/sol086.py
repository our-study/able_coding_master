import math 
 
def find_minimal_original_grid(N, M, grid): 
    gcd_nm = math.gcd(N, M) 
    # Iterate K from gcd_nm down to 1 to find the largest possible K 
    for K in range(gcd_nm, 0, -1): 
        if N % K != 0 or M % K != 0: 
            continue  # K must divide both N and M 
        r = N // K 
        c = M // K 
        # Extract the candidate original grid 
        candidate = [row[:c] for row in grid[:r]] 
        # Verify if tiling the candidate K times vertically and horizontally matches the original grid 
        valid = True 
        for i in range(N): 
            for j in range(M): 
                if grid[i][j] != candidate[i % r][j % c]: 
                    valid = False 
                    break 
            if not valid: 
                break 
        if valid: 
            return candidate 
    # If no smaller grid is found, return the original grid 
    return grid 
 
def main(): 
    import sys 
    import sys 
    # Read N and M 
    try: 
        N, M = map(int, sys.stdin.readline().split()) 
    except: 
        N, M = map(int, input().split()) 
    # Read the grid 
    grid = [] 
    for _ in range(N): 
        try: 
            line = sys.stdin.readline().rstrip('\
') 
            if not line: 
                line = input().rstrip('\
') 
        except: 
            line = input().rstrip('\
') 
        # Ensure the line has exactly M characters 
        while len(line) < M: 
            line += ' ' 
        grid.append(line[:M]) 
    # Find the minimal original grid 
    original_grid = find_minimal_original_grid(N, M, grid) 
    # Output the original grid 
    for row in original_grid: 
        print(row) 
 
if __name__ == \"__main__\": 
    main() 
