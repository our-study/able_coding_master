from sys import stdin

coin_type, price = map(int, stdin.readline().split())

coins =[]

for i in range(coin_type):
    coins.append(int(stdin.readline().rstrip()))
    

dp = [10001]*(price+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, price+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[price]== 10001:
    print(-1)
else:
    print(dp[price])
    
