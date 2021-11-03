# https://www.acmicpc.net/problem/14938
import sys
import heapq

input = sys.stdin.readline

n, k, m = map(int,input().split())
item = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
INF = int(1e9)
result = -1

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q : 
        dist, now = heapq.heappop(q) 
        if distance[now] < dist :
            continue
        for next_, next_cost in graph[now] :
            cost = dist + next_cost
            if cost < distance[next_]:
                distance[next_] = cost
                heapq.heappush(q,(cost, next_))

    countItem = 0 
    for d in range(1, n+1) :
        if distance[d] != INF and distance[d] <= k : 
            countItem += item[d]

    return countItem

for i in range(1,n+1) :
    result = max(result, dijkstra(i))

print(result)
    
