#https://www.acmicpc.net/problem/1504

# 조건 
# 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
# 단, 임의로 주어진 두 정점은 반드시 통과해야 한다.
# 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.

import heapq
import sys

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(e) :
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())

def dijkstra(start) :
    distance = [INF] * (n+1)
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

    return distance

result = dijkstra(1) 
v1_result = dijkstra(v1)
v2_result = dijkstra(v2) 

answer = min(result[v1]+v1_result[v2]+v2_result[n], result[v2]+v2_result[v1]+v1_result[n])

if answer >= INF or answer < 0 :
    print(-1) 
else : 
    print(answer) 