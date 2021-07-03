import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF] * (n+1)

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

index = -1
value = -1
same = 0
for i in range(1, n+1):
    if value < distance[i]:
        index = i
        value = distance[i]
        smae = 1
    elif value == distance[i]:
        same += 1

print(index, value, same)

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
