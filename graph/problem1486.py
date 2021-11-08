# https://www.acmicpc.net/problem/1486

from collections import deque
import math
n, m, t, d = map(int,input().split())
dx, dy = [0,1,0,-1], [1,0,-1,0]
INF = int(1e9)
graph = [[0] * m for _ in range(n)]
start = [[INF] * m for _ in range(n)]
end = [[INF] * m for _ in range(n)]

for i in range(n) :
    lst = list(input().strip('\n'))
    for j in range(m) :
        if 'A' <= lst[j] <= 'Z' :
            graph[i][j] = ord(lst[j]) - 65
        else :
            graph[i][j] = ord(lst[j]) - 71

while q : 
    q = deque([(0,0)])
    start[0][0] = 0
    x, y = q.popleft()
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if abs(graph[x][y] - graph[nx][ny]) > t : continue
            time = -1
            if graph[x][y] >= graph[nx][ny]  :
                time = 1 + start[x][y] 
            else : 
                time = start[x][y] + (abs(graph[nx][ny] - graph[x][y]) ** 2)
                
            if time != -1 and start[nx][ny] > time and time <= d :
                start[nx][ny] = time 
                q.append((nx,ny))                        
    
while q : 
    x, y = q.popleft()
    q = deque([(0,0)])
    end[0][0] = 0
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if abs(graph[x][y] - graph[nx][ny]) > t : continue
            time = -1
            if graph[x][y] > graph[nx][ny]  :
                time = end[x][y] + (abs(graph[nx][ny] - graph[x][y]) ** 2)
            else : 
                time = 1 + end[x][y] 
            if time != -1 and end[nx][ny] > time and time <= d :
                    end[nx][ny] = time 
                    q.append((nx,ny))    

ans = graph[0][0]
for i in range(n) :
    for j in range(m) :
        if start[i][j] != INF and end[i][j] != INF and ans < graph[i][j] :
            if start[i][j] + end[i][j] <= d :
                ans = graph[i][j]
print(ans)

