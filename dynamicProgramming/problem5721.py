# https://www.acmicpc.net/problem/5721

import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n + m == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    dp = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0][1] = graph[1][0]

    for i in range(n):
        for j in range(1, m):
            dp[i][j][1] = dp[i][j-1][0] + graph[i][j]
            dp[i][j][0] = max(dp[i][j][0], dp[i][j-1][1])

    # value : 현재 i 번째 행에서 얻을 수 있는 최대 사탕
    value = [0] * n
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp = max(tmp, dp[i][j][0], dp[i][j][1])
        value[i] = tmp

    row = [[0] * 2 for _ in range(n)]
    row[0][1] = value[0]

    for i in range(1, n):
        row[i][1] = row[i-1][0] + value[i]
        row[i][0] = max(row[i-1][0], row[i-1][1])
    print(max(row[n - 1][0], row[n - 1][1]))
