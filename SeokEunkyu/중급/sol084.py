def count_rectangles_with_sum_10(grid, n, m): 
    count = 0 
 
    # 모든 가능한 직사각형 구역 탐색 
    for r1 in range(n): 
        for c1 in range(m): 
            for r2 in range(r1, n): 
                for c2 in range(c1, m): 
                    # 직사각형 내부의 합 계산 
                    current_sum = 0 
                    for i in range(r1, r2 + 1): 
                        for j in range(c1, c2 + 1): 
                            current_sum += grid[i][j] 
                     
                    # 합이 10인 경우 카운트 증가 
                    if current_sum == 10: 
                        count += 1 
 
    return count 
 
# 입력 처리 
n, m = map(int, input().split()) 
grid = [list(map(int, input().split())) for _ in range(n)] 
 
# 결과 출력 
result = count_rectangles_with_sum_10(grid, n, m) 
print(result) 
