# https://www.acmicpc.net/problem/1719

import sys
input = sys.stdin.readline

n ,m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]
result = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    graph[i][i] = 0

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a][b] =c 
    graph[b][a] = c
    result[a][b] = b
    result[b][a] = a


for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            if graph[a][b] > graph[a][k] + graph[k][b] :
                graph[a][b] = graph[a][k] + graph[k][b]
                result[a][b] = result[a][k]


for i in range(1, n+1) :
    for j in range(1, n+1) :
        if result[i][j] == 0 :
            print('-', end = ' ')
        else :
            print(result[i][j], end = ' ')
    print()
