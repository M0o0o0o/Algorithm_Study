# https://www.acmicpc.net/problem/2229

n = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = max(dp[i-1], abs(lst[i] - lst[i-1]) + dp[i-2])

print(max(dp))
