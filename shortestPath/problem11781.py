# https://www.acmicpc.net/problem/11781

import heapq
import sys
input = sys.stdin.readline

n, m, s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = float('inf')
distance = [INF] * (n+1)

for _ in range(m):
    a, b, l, t1, t2 = map(int, input().split())
    graph[a].append((b, l, t1))
    graph[b].append((a, l, t2))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for node, length, jam in graph[now]:
        cost = dist + length
        if jam == 1 and ((dist <= s <= dist + length) or (dist <= e <= dist + length)):
            if dist <= s <= cost:
                cost = dist + (s - dist)
                remain_d = length - s  # 3
                remain_m = e-s  # 8
                remain_m_d = remain_m / 2  # 4
                if remain_d <= remain_m_d:
                    cost += remain_d * 2
                else:
                    cost += remain_m + (remain_d - remain_m_d)
            else:  # 시작부터 퇴근시간에 걸리는 경우
                minute = e - dist  # 5분
                minute_d = minute / 2
                cost = dist + minute + (length - minute_d)
        if cost < distance[node]:
            distance[node] = cost
            heapq.heappush(q, (cost, node))

ans = 0
for d in distance:
    if d == float('inf'):
        continue
    ans = max(ans, d)
if int(ans) == ans:
    print(int(ans))
else:
    print(ans)
