import sys

data = sys.stdin.read().splitlines()

N = int(data[0])  
coins = [list(map(int, data[i + 1].split())) for i in range(N)]  

dp = [[0] * (i + 1) for i in range(N)]

dp[0][0] = coins[0][0]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + coins[i][0]  
    for j in range(1, i + 1):
        if j < i:  
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + coins[i][j]
        else:  
            dp[i][j] = dp[i-1][j-1] + coins[i][j]
            
result = max(dp[N-1])
print(result)
