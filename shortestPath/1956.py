#https://www.acmicpc.net/problem/1956
#플로이드 워샬을 이용해 풀이했다.

import heapq
import sys

input = sys.stdin.readline

v,e = map(int,input().split())
INF = int(1e9)
graph = [[INF for _ in range(v+1)] for _ in range(v+1)]


for i in range(1,v+1) :
    for j in range(1, v+1) :
        if i == j :
            graph[i][j] = 0

for _ in range(e) :
    a, b, c = map(int,input().split())
    graph[a][b] = c 

for k in range(1, v+1) :
    for i in range(1,v+1) :
        for j in range(1,v+1) :
            if  i == j :
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


ans = INF 
for i in range(1,v+1) :
    for j in range(1, v+1) :
        if i == j : 
            continue
        else : 
            if graph[i][j] != INF and graph[j][i] != INF :
                ans = min(ans, graph[i][j] + graph[j][i])

if ans >= INF : 
    print(-1) 
else : 
    print(ans) 


