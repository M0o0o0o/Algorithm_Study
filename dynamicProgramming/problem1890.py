# https://www.acmicpc.net/problem/1890


n = int(input())
graph = []
dp = [[0] * n for _ in range(n)]
for _ in range(n) :
    graph.append(list(map(int,input().split())))

dp[0][0] = 1

for i in range(n) :
    for j in range(n) :
        if (i, j) == (n-1, n-1) : break
        d = graph[i][j]
        if i + d < n : 
            dp[i+d][j] += dp[i][j]
        if j + d < n :
            dp[i][j+d] += dp[i][j]

print(dp[n-1][n-1])


