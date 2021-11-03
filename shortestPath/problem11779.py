# https://www.acmicpc.net/problem/11779

import heapq
import copy
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
parent = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))


s, e = map(int,input().split())

q = []
heapq.heappush(q,(0,s))
distance[s] = 0
parent[s].append(s)

while q : 
    dist, now = heapq.heappop(q) 
    if distance[now] < dist :
        continue
    for next_, next_cost in graph[now] :
        cost = dist + next_cost
        if cost < distance[next_] :
            distance[next_] = cost
            heapq.heappush(q,(cost, next_))
            parent[next_] = []
            for p in parent[now] :
                parent[next_].append(p)
            parent[next_].append(next_)   

print(distance[e])
print(len(parent[e]))
for p in parent[e] :
    print(p, end = ' ')
