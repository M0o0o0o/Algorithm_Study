# https://www.acmicpc.net/problem/4811

import sys
input = sys.stdin.readline

# dp[i][j] = w(i), h(j)로 만들 수 있는 경우의 수
dp = [[0 for _ in range(31)] for _ in range(31)]

for j in range(1, 31):
    dp[0][j] = 1

for i in range(1, 31):
    for j in range(30):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i][j-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][0])
