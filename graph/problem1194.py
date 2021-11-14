# https://www.acmicpc.net/problem/1194

import sys
input = sys.stdin.readline
from collections import deque

dx, dy = [0,1,0,-1], [1,0,-1,0]
x,y = 0, 0
n, m = map(int, input().split())
graph = []
visited = [[[0]*64 for _ in range(m)] for _ in range(n)]
ans = -1

for i in range(n) :
    graph.append(list(input().strip('\n')))
    for j in range(m) :
        if graph[i][j] == '0' :
            x, y = i, j
            graph[i][j] = '.'
            
q = deque([[x,y,0]])

while q:
        x, y, z = q.popleft()
        if graph[x][y] == '1':
            ans = visited[x][y][z] 
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and visited[nx][ny][z] == 0:
                    if graph[nx][ny].islower():
                        nz = z | (1 << (ord(graph[nx][ny]) - ord('a')))
                        if visited[nx][ny][nz] == 0:
                            visited[nx][ny][nz] = visited[x][y][z] + 1
                            q.append([nx, ny, nz])
                    elif graph[nx][ny].isupper():
                        if z & (1 << (ord(graph[nx][ny]) - ord('A'))):
                            visited[nx][ny][z] = visited[x][y][z] + 1
                            q.append([nx, ny, z])
                    else:
                        visited[nx][ny][z] = visited[x][y][z] + 1
                        q.append([nx, ny, z])

print(ans)

