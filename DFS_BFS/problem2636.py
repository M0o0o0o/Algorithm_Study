# https://www.acmicpc.net/problem/2636

from collections import deque

def check(x,y) :
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 3 :
            return True
    return False

def bfs() :
    while q : 
        x, y = q.popleft()
        graph[x][y] = 3 
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 :
                graph[nx][ny] = 3
                q.append((nx,ny))


n, m = map(int,input().split())
graph = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for _ in range(n) :
    graph.append(list(map(int,input().split())))
t, c = 0, 0
q = deque([(0,0)])

while True :
    count = 0
    bfs()

    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 and check(i,j) :
                count += 1
                graph[i][j] = 0
                q.append((i,j))

    if count == 0 : break
    t += 1
    c = count

print(t)
print(c)