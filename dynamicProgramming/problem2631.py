# https://www.acmicpc.net/problem/2631

n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [1] * (n)

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
