# https://www.acmicpc.net/problem/1613

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
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
                

for _ in range(int(input())) :
    a, b = map(int, input().split())
    if graph[a][b] != INF : print(-1)
    elif graph[b][a] != INF : print(1)
    else : print(0)