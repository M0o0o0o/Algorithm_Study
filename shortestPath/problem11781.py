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

        if not jam or dist >= e or (dist+length) <= s : 
            cost = length
        elif dist >= s and (dist + length) >= e : 
            m = e - dist
            m_d = m / 2 
            cost = m + (length - m_d)
        elif dist >= s and (dist + length) < e : 
            m = e - dist
            m_d = m / 2
            if m_d >= length : 
                cost = length * 2 
            else : 
                cost = cost = m + (length - m_d)
        elif dist < s and length < e : 
            m = e-s
            m_d = m / 2
            cost = s - dist 
            length -= s
            if m_d >= length : 
                cost += length * 2 
            else : 
                cost = cost = m + (length - m_d)
        cost += dist
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
