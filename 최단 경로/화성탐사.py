import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(1e9)
for i in range(int(input())):
    n = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF]*n for _ in range(n)]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx >= 0 and mx < n and my >= 0 and my < n:
                cost = dist + graph[mx][my]
                if cost < distance[mx][my]:
                    distance[mx][my] = cost
                    heapq.heappush(q, (cost, mx, my))

    print(distance[n-1][n-1])


# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
