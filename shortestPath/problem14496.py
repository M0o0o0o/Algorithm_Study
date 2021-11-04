# https://www.acmicpc.net/problem/14496

import heapq
import sys
input = sys.stdin.readline

s, e = map(int,input().split())
n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
INF = sys.maxsize
distance = [INF] * (n+1)


for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q : 
        dist, now = heapq.heappop(q) 
        if distance[now] < dist :
            continue
        for next_ in graph[now] :
            cost = dist + 1
            if cost < distance[next_]:
                distance[next_] = cost
                heapq.heappush(q,(cost, next_))

dijkstra(s)

if distance[e] == INF : 
    print(-1)
else :
    print(distance[e])