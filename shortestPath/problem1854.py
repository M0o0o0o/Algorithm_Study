# https://www.acmicpc.net/problem/1854

import heapq
import sys 
input = sys.stdin.readline

n, m, k = map(int,input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [[] for _ in range(n+1)]
result = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

q = []
heapq.heappush(q,(0,1))
heapq.heappush(distance[1], 0)
while q : 
    dist, now = heapq.heappop(q) 
    for next_, next_cost in graph[now] :
        cost = dist + next_cost
        if len(distance[next_]) < k :
            heapq.heappush(distance[next_], -cost)
            heapq.heappush(q,(cost, next_))
            
        elif -distance[next_][0] > cost : 
            heapq.heappop(distance[next_])
            heapq.heappush(distance[next_], -cost)
            heapq.heappush(q,(cost, next_))
                    

for i in range(1, n+1) :
    if len(distance[i]) < k :
        print(-1)
    else :
        print(-heapq.heappop(distance[i]))
