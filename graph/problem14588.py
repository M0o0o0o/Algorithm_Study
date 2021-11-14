# https://www.acmicpc.net/problem/14588

import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
line = [0]
graph =[[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    a,b = map(int, input().split())
    line.append((a,b))

for i in range(1,n+1) :
    for j in range(i+1, n+1) :
        (a,b), (c,d) = line[i], line[j]
        if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d :
            graph[i][j] = 1
            graph[j][i] = 1
 
for i in range(1,n+1) :
    graph[i][i] = 0 
    
for k in range(1, n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] +  graph[k][j])
      
for _ in range(int(input())) :
    a, b = map(int, input().split())
    if graph[a][b] == INF :
        print(-1)
    else :
        print(graph[a][b])

