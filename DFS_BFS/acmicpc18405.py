# https://www.acmicpc.net/problem/18405
# 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나
# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 낙나다.
# 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 
# 다른 바이러스가 들어갈 수 없다.

import heapq

# n x n 시험관, k : 바이러스의 종류
n, k = map(int, input().split()) 
graph = []
q = []

for i in range(n) :
    graph.append(list(map(int,input().split())))

for i in range(n) :
    for j in range(n) :
        if graph[i][j] > 0 :
            heapq.heappush(q, (graph[i][j], (i,j)))


s, x, y = map(int,input().split())
x -= 1 
y -= 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]


for _ in range(s) :
    q2 = []
    while q : 
        virus, (cx, cy) = heapq.heappop(q)
        for i in range(4) :
            mx = cx + dx[i]
            my  = cy + dy[i] 
        
            if mx >= 0 and mx < n and my >= 0 and my < n and graph[mx][my] == 0 :
                graph[mx][my] = virus
                heapq.heappush(q2, (virus, (mx,my)))

    q = q2


print(graph[x][y])