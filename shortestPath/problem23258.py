# https://www.acmicpc.net/problem/23258

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
INF = int(1e9)
graph = [[[INF for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1) :
    buf = [0] + list(map(int, input().split()))
    for j in range(1, n+1) :
        graph[0][i][j] = buf[j]
        if graph[0][i][j] == 0 and i != j :  graph[0][i][j] = INF
        
    
for m in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1,n+1) :
            graph[m][i][j] = min(graph[m-1][i][j], graph[m-1][i][m] + graph[m-1][m][j])
            

for _ in range(q) :
    c, a, b = map(int, input().split())
    print(graph[c-1][a][b] if graph[c-1][a][b] != INF else -1)
    
    