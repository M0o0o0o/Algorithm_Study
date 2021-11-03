# https://www.acmicpc.net/problem/1162

import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

q = []
heapq.heappush(q,(0,1,0))
distance[1] = 0

while q : 
    dist, now, count = heapq.heappop(q) 
    for next_, next_cost in graph[now] :
        cost = dist + next_cost

        if cost < distance[next_] :
            distance[next_] = cost
            print(next_, distance[next_])
            heapq.heappush(q,(cost, next_, count))

        if count < k and dist < distance[next_] :
            distance[next_] = dist  
            print(next_, distance[next_])
            heapq.heappush(q,(dist, next_, count + 1))

print(distance[n])