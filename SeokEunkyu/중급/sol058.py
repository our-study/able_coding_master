def max_coins_in_triangle(n, coins):
    # DP 테이블 초기화
    dp = [[0] * n for _ in range(n)]
    
    # 맨 아래층의 동전 개수를 그대로 DP 테이블에 복사
    dp[n-1] = coins[n-1]
    
    # 아래에서부터 위로 올라가며 DP 테이블 갱신
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + coins[i][j]
    
    # 최종적으로 정상의 값이 최대 동전 개수
    return dp[0][0]

# 입력 받기
n = int(input())
coins = []
for i in range(n):
    coins.append(list(map(int, input().split())))

# 결과 출력
print(max_coins_in_triangle(n, coins))
