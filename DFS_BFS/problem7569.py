# https://www.acmicpc.net/problem/7569
from collections import deque
import sys 

m, n, h = map(int,sys.stdin.readline().split())
graph = []
answer = -1
dx, dy, dh = [0,1,0,-1], [1,0,-1,0], [-1,1]
q = deque([])
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

for _ in range(h) :
    lst = []
    for _ in range(n) :
        lst.append(list(map(int,sys.stdin.readline().split())))
    graph.append(lst)

def bfs() : 
    global q
    global answer
    
    while q : 
        v, x, y, c = q.popleft()
        answer = max(answer, c)
        for i in range(4) :
            nx = x + dx[i] 
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[v][nx][ny] == 0  :
                graph[v][nx][ny] = 1
                q.append((v,nx,ny,c+1))
                
        for i in range(2) :
            nh = v + dh[i]
            if 0 <= nh < h and graph[nh][x][y] == 0 :
                graph[nh][x][y] = 1 
                q.append((nh,x,y,c+1))


for v in range(h) :
    for i in range(n) :
        for j in range(m) : 
            if graph[v][i][j] == 1 and not visited[v][i][j] :
                q.append((v,i,j,0))
                visited[v][i][j] = True

bfs()

zero = False
for i in range(h) :
    for j in range(n) :
        if graph[i][j].count(0) > 0 :
            zero = True
            break

if zero :
    print(-1)
else :
    print(answer)

