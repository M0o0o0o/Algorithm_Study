# https://www.acmicpc.net/problem/4179

from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip('\n')) for _ in range(n)]
dx, dy = [0,1,0,-1], [1,0,-1,0]
visited =[[False for _ in range(m)] for _ in range(n)]
fq = deque([])
jq = deque([])
ans = int(1e9)
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 'J' :
            graph[i][j] = '.'
            jq.append((i,j, 0))
            visited[i][j] = True
        if graph[i][j] == 'F' : 
            fq.append((i,j))
            graph[i][j] = 0
            
while fq : 
    x,y = fq.popleft()
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i] 
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.' : 
            graph[nx][ny] = graph[x][y] + 1
            fq.append((nx,ny))

print(graph)
            
while jq : 
    x, y, t = jq.popleft()
    t += 1
    if x == 0 or x == n-1 or y == 0 or y == m-1 : 
            ans = t 
            break
    for i in range(4) : 
        nx, ny = x + dx[i], y + dy[i] 
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#' and graph[nx][ny] > t and not visited[nx][ny] : 
            jq.append((nx, ny, t))
            visited[nx][ny] = True
            
if ans == int(1e9) :
    print('IMPOSSIBLE')
else :
    print(ans)
            
