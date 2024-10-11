def count_tilings(N): 
    # 초기 조건 설정 
    dp = [0] * (N + 1) 
    dp[0] = 1  # 그리드가 없는 경우 
    if N >= 1: 
        dp[1] = 0  # 3x1 그리드는 불가능 
    if N >= 2: 
        dp[2] = 3  # 3x2 그리드를 채우는 경우의 수는 3 
    if N >= 3: 
        dp[3] = 0  # 3x3 그리드는 불가능 
 
    # 점화식을 이용하여 dp 테이블 채우기 
    for i in range(4, N + 1): 
        if i % 2 != 0: 
            dp[i] = 0  # N이 홀수인 경우 불가능 
        else: 
            dp[i] = 4 * dp[i - 2] - dp[i - 4] 
     
    return dp[N] 
 
# 입력 받기 
if __name__ == \"__main__\": 
    import sys 
    N_input = int(sys.stdin.readline()) 
    result = count_tilings(N_input) 
    print(result) 
