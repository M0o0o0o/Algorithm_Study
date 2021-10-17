# https://www.acmicpc.net/problem/4485

import heapq

INF = int(1e9)
index = 1
dx, dy = [0,1,0,-1], [1,0,-1,0]

while True : 
    n = int(input()) 
    if n == 0 : break

    graph, distance = [], [[INF] * n for _ in range(n)]

    for _ in range(n) :
        graph.append(list(map(int,input().split())))

    q = []
    distance[0][0] = graph[0][0] 
    heapq.heappush(q,(graph[0][0], 0, 0))

    while q  :
        dist, x, y = heapq.heappop(q) 
        if distance[x][y] < dist : continue
        for d in range(4) :
            nx, ny = x + dx[d], y + dy[d] 
            if 0 <= nx < n and 0 <= ny < n :
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny] :
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost, nx, ny))

    print("Problem " + str(index) + ": " + str(distance[n-1][n-1]))
    index += 1