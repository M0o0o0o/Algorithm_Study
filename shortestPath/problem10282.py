# https://www.acmicpc.net/problem/10282
import sys 
import heapq

input = sys.stdin.readline
INF = int(1e9)

for _ in range(int(input())) :
    n, d, start = map(int,input().split())
    graph = [[] * (n+1) for _ in range(n+1)]

    for _ in range(d) :
        a, b, c = map(int,input().split())
        graph[b].append((a,c))

    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0 
    while q :
        dist, now = heapq.heappop(q)
        if dist > distance[now] : continue
        for node, _dist in graph[now] :

            cost = dist + _dist 
            if cost < distance[node] :
                distance[node] = cost 
                heapq.heappush(q,(cost, node))
                

    count, total = 0, 0
    for i in distance :
        if i != INF :
            count += 1
            total = max(total, i)

    print(count, total)

