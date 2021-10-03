# https://www.acmicpc.net/problem/1937

import sys
sys.setrecursionlimit(10**5)


def dfs(i, j) :
    if dp[i][j] < 0 :
        dp[i][j] = 0
        for d in range(4) :
            x, y = i + dx[d], j + dy[d]
            if 0 <= x < n and 0 <= y < n and graph[i][j] > graph[x][y] :
                dp[i][j] = max(dp[i][j], dfs(x,y))
        dp[i][j] += 1
    return dp[i][j]

n = int(input())
graph = []
dp = [[-1] * n for _ in range(n)]
dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]
answer = 0 

for _ in range(n) :
    graph.append(list(map(int,input().split())))


for i in range(n) :
    for j in range(n) :
        answer = max(answer, dfs(i,j))

print(answer)