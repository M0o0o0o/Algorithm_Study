# https://www.acmicpc.net/problem/10159

import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    graph[i][i] = 0

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                

for i in range(1,n+1) :
    cnt = 0
    for j in range(1, n+1) :
        if i == j : continue
        if graph[i][j] == INF and graph[j][i] == INF:
            cnt += 1
    print(cnt)
