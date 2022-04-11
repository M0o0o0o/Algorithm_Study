# https://programmers.co.kr/learn/courses/30/lessons/12978

from heapq import heappush, heappop


def solution(n, road, k):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
    distance = [INF] * (n+1)
    distance[1] = 0

    q = []
    heappush(q, (0, 1))
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    ans = 0
    for d in distance:
        if d <= k:
            ans += 1
    return ans


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
      [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
