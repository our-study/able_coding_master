import sys

N = int(sys.stdin.readline())
sharks = list(map(int, sys.stdin.readline().split()))

def max_chain(sharks):
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if sharks[j] < sharks[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(max_chain(sharks))
