# https://www.acmicpc.net/problem/1535


n = int(input())
bad = list(map(int, input().split()))
good = list(map(int, input().split()))
bad, good = [0] + bad, [0] + good
dp = [[0 for _ in range(101)]for _ in range(n+1)]

for i in range(n+1):
    for j in range(1, 101):
        if bad[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bad[i]] + good[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
