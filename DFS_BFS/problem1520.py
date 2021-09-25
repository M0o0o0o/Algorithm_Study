# https://www.acmicpc.net/problem/1520

from collections import deque
n, m = map(int,input().split())
answer = 0
queue = deque([])
graph = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(n) :
    graph.append(list(map(int,input().split())))

queue.append((0,0))

while queue : 
    x, y = queue.popleft()
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] < graph[x][y] :
            if nx == n-1 and ny == m-1 :
                answer += 1
                break
            queue.append((nx,ny))

print(answer)


