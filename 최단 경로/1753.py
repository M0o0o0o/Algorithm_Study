#https://www.acmicpc.net/problem/1753

import heapq
import sys

input = sys.stdin.readline

v, e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e9)
distance = [INF] * (v+1) 

for _ in range(e) :
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if(dist > distance[now]) : 
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, len(distance)) :
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])
