# https://www.acmicpc.net/problem/1238
import heapq

n, m, target = map(int,input().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
answer = [INF] * (n)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start) :
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q  :
        dist, now = heapq.heappop(q)
        if distance[now] < dist : 
            continue 
        for (next_n, next_c) in graph[now] :
            cost = dist + next_c 
            if distance[next_n] > cost :
                distance[next_n] = cost
                heapq.heappush(q,(cost, next_n))

    return distance


for i in range(1, n+1) :
    _distance = dijkstra(i)
    answer[i-1] = _distance[target]

_distance = dijkstra(target)

for i in range(1, n+1) :
    answer[i-1] += _distance[i]

print(max(answer))