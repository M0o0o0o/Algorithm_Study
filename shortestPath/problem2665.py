# https://www.acmicpc.net/problem/2665

import heapq

n = int(input())

INF = int(1e9)
dx, dy = [0,1,0,-1], [1,0,-1,0]
distance = [[INF] * n for _ in range(n)]
graph, q = [], []

for _ in range(n) :
    graph.append(list(input()))

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == '1' : graph[i][j] = 0
        else : graph[i][j] = 1

distance[0][0] = 0
heapq.heappush(q, (0,0,0))

while q :
    dist, x, y = heapq.heappop(q) 
    if distance[x][y] < dist : continue
    for d in range(4) :
        nx, ny = x + dx[d], y + dy[d] 
        if 0 <= nx < n and 0 <= ny < n :
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny] :
                distance[nx][ny] = cost
                heapq.heappush(q,(cost, nx, ny))

print(distance[n-1][n-1])
