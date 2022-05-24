# https://www.acmicpc.net/problem/2302

n, m = int(input()), int(input())
dp = [1] * (n+2)
vip = [int(input()) for _ in range(m)] + [n+1]
ans = 1

for i in range(2, n+2):
    if i in vip:
        ans *= dp[i-1]
        continue
    if i-1 in vip:
        continue
    dp[i] = dp[i-1] + dp[i-2]
print(ans)
