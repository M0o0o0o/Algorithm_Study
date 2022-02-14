# https://www.acmicpc.net/problem/1743
from collections import deque

def bfs(i, j) :
    q = deque([(i,j)])
    count = 1
    while q : 
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '#' :
                q.append((nx,ny))
                graph[nx][ny] = '.'
                count += 1
    return count
                
n, m, k = map(int, input().split())
graph =[['.' for i in range(m)] for _ in range(n)]
dx, dy = [0,1,0,-1], [1,0,-1,0]
ans = 0

for _ in range(k) :
    x, y = map(int, input().split())
    graph[x-1][y-1] = '#'
    
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == '#' : 
            graph[i][j] = '.'
            ans = max(bfs(i,j), ans)
            
print(ans)