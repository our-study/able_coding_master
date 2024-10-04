import sys 
 
def find_max_square_area(N, M, grid): 
    \"\"\" 
    주어진 그리드에서 같은 숫자를 가진 네 꼭짓점으로 이루어진 정사각형 중 가장 넓은 넓이를 찾습니다. 
     
    Parameters: 
    - N (int): 그리드의 세로줄 수 
    - M (int): 그리드의 가로줄 수 
    - grid (list of list of int): 그리드의 각 칸에 적힌 숫자 
     
    Returns: 
    - int: 가장 넓은 정사각형의 넓이 
    \"\"\" 
    max_area = 1  # 최소 정사각형의 넓이는 1 (2x2 칸) 
     
    # 가능한 최대 변의 길이 (s는 변의 길이 - 1) 
    # s=1 -> 2x2 칸, s=2 -> 3x3 칸, ... 
    max_s = min(N, M) - 1 
     
    for s in range(max_s, 0, -1): 
        # 정사각형의 변의 길이가 s일 때, 0-based 인덱스 
        for i in range(N - s): 
            for j in range(M - s): 
                top_left = grid[i][j] 
                top_right = grid[i][j + s] 
                bottom_left = grid[i + s][j] 
                bottom_right = grid[i + s][j + s] 
                 
                if top_left == top_right == bottom_left == bottom_right: 
                    area = (s + 1) * (s + 1) 
                    return area  # 가장 큰 정사각형의 넓이를 찾았으므로 즉시 반환 
     
    return max_area  # 모든 정사각형을 검사했지만, 문제 조건상 최소 하나는 존재하므로 반환 
 
def main(): 
    \"\"\" 
    메인 함수: 입력을 받고, 가장 넓은 정사각형의 넓이를 출력합니다. 
    \"\"\" 
    input = sys.stdin.read 
    data = input().splitlines() 
     
    if not data: 
        print(0) 
        return 
     
    # 첫 번째 줄에서 N과 M을 읽습니다. 
    N, M = map(int, data[0].strip().split()) 
     
    # 다음 N개의 줄에서 그리드를 읽습니다. 
    grid = [] 
    for i in range(1, N + 1): 
        if i >= len(data): 
            grid.append([]) 
        else: 
            row = list(map(int, data[i].strip().split())) 
            grid.append(row) 
     
    # 가장 넓은 정사각형의 넓이를 찾습니다. 
    max_area = find_max_square_area(N, M, grid) 
     
    # 결과를 출력합니다. 
    print(max_area) 
 
if __name__ == \"__main__\": 
    main() 
