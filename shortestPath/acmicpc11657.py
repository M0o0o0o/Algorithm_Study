# https://www.acmicpc.net/problem/11657

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph) :
    distance = [INF] * len(graph)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

distnace = dijkstra(1, graph)


print(distnace)