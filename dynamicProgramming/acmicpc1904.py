# https://www.acmicpc.net/problem/1904

n = int(input())

dp = [0] * n

for i in range(n) :
    if i == 0 :
        dp[i] = 1
    elif i == 1 :
        dp[i] = 2
    else :
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 15746

print(dp[n-1])


