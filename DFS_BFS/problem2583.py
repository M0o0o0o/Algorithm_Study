# https://www.acmicpc.net/problem/2583

from collections import deque
n, m, k = map(int,input().split())
graph = [[False] * m for _ in range(n)]
queue = deque([])

for _ in range(k) :
    x,y,x1,y1 = map(int,input().split())
    for i in range(y, y1) :
        for j in range(x, x1) :
            graph[i][j] = True

answer = [0, []]
dx = [0,1,0,-1] 
dy = [1,0,-1,0]

def bfs() :
    global queue 
    count = 1
    while queue :   
        x,y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i] 
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny] : 
                count +=1 
                graph[nx][ny] = True 
                queue.append((nx,ny))
    return count

for i in range(n) :
    for j in range(m) :
        if not graph[i][j] :
            queue.append((i,j))
            answer[0] += 1
            graph[i][j] = True
            answer[1].append(bfs())

print(answer[0])
answer[1].sort()
for i in answer[1] :
    print(i, end =' ')


