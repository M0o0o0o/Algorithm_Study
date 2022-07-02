# https://www.acmicpc.net/problem/16118

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)


def fox_dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance = [INF] * (n+1)
    distance[start] = 0

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            contin
        for i in graph[now]:
            node, nodeCost = i[0], i[1] * 2
            cost = dist + nodeCost
            if cost < distance[node]:
                distance[node] = cost
                heappush(q, (cost, node))
    return distance


def wolf_distance(start):
    q = []
    heappush(q, (0, start, 0))  # 홀수에는 두 배
    distance = [[INF for _ in range(2)]for _ in range(n+1)]
    distance[start][0] = 0

    while q:
        dist, now, mode = heappop(q)
        if distance[now][mode] < dist:
            continue
        for i in graph[now]:
            nextMode = 1 if mode == 0 else 0
            node, nodeCost = i
            cost = dist + nodeCost if nextMode == 1 else dist + \
                (nodeCost * 4)
            if cost < distance[node][nextMode]:
                distance[node][nextMode] = cost
                heappush(q, (cost, node, nextMode))

    return distance


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

fd = fox_dijkstra(1)
wd = wolf_distance(1)


ans = 0
for i in range(1, n+1):
    if fd[i] < wd[i][0] and fd[i] < wd[i][1]:
        ans += 1

print(ans)
