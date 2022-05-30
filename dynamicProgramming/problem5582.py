# https://www.acmicpc.net/problem/5582
import sys
input = sys.stdin.readline
a, b = input().strip('\n'), input().strip('\n')
dp = [[0 for _ in range(len(b) + 1)]for _ in range(len(a) + 1)]
ans = 0
for i in range(1, len(a)+1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])

print(ans)
