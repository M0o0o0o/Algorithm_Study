# https://www.acmicpc.net/problem/2293

n, target = map(int, input().split())

dp = [0] * (100001)
for _ in range(n) :
    m = int(input())
    dp[m] += 1
    for i in range(1, target+1) :
        if i - m  >= 1 :
            dp[i] += dp[i - m]
print(dp[target])