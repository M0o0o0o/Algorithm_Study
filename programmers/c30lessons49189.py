# https://programmers.co.kr/learn/courses/30/lessons/49189

from heapq import heappush, heappop
INF = int(1e9)


def solution(n, edge):
    graph = [[] for i in range(n+1)]
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    distance = [INF] * (n+1)

    q = []
    heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heappush(q, (cost, i))
    distance = [0 if d == INF else d for d in distance]
    return distance.count(max(distance))


print(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
