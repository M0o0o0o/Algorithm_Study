# https://www.acmicpc.net/problem/2458

import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
INF = int(1e9)
graph = [[INF] * (n+2) for _ in range(n+1)]

for i in range(1,n+1) :
    graph[i][i] = 0
    graph[i][n+1] = 0

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if graph[i][j] not in [0, INF] : 
            graph[j][n+1] += 1
            graph[i][j] = 1

result = 0

for i in range(1,n+1) :
    if graph[i][:n+1].count(1) + graph[i][n+1] == n-1 :
        result += 1

print(result)