# https://www.acmicpc.net/problem/11562


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    graph[i][i] = 0

for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a][b] = 0
    if c == 1 : graph[b][a] = 0  
    else : graph[b][a] = 1

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
for _ in range(int(input())) :
    a, b = map(int, input().split())
    print(graph[a][b])

