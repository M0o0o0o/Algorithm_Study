# https://www.acmicpc.net/problem/2307

import heapq
import sys
input = sys.stdin.readline

def d() :
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist : continue 
        for i in range(1, n+1) :
            if graph[now][i] == INF : continue
            next, dist_ = i, graph[now][i]
            cost = dist + dist_ 
            if distance[next] > cost :
                heapq.heappush(q,(cost, next))
                distance[next] = cost
            
    return distance[n]

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
edges = []
for _ in range(m) :
    a,b,c=  map(int, input().split())
    edges.append((a,b,c))
    graph[a][b] = c
    graph[b][a] = c
    

small = d()
big = 0 

for a,b,c in edges : 
    graph[a][b], graph[b][a] = INF, INF
    big = max(big, d())
    graph[a][b], graph[b][a] = c, c
    

if big == INF : print(-1)
else : print(big - small)