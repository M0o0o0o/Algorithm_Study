# https://www.acmicpc.net/problem/10026

from collections import deque

n = int(input())
graph = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque([])

for _ in range(n) :
    graph.append(list(input()))

answer = [0,0]

def bfs(visited, color, check) :
    global queue
    while queue : 
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                if check and (color == 'R' or color == 'G') and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') :
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == color :
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    


for i in range(2) :
    visited = [[False] * n for _ in range(n)]
    queue = deque([])
    count = 0
    for x in range(n) :
        for y in range(n) :
            if visited[x][y] == False :
                count += 1
                queue.append((x,y))
                visited[x][y] = True
                if i == 1 :
                    bfs(visited, graph[x][y], True)
                else :
                    bfs(visited, graph[x][y], False)

    if i == 0 : answer[0] = count
    else : answer[1] = count

print(answer[0], answer[1])