# https://www.acmicpc.net/problem/2206

from collections import deque

n, m = map(int,input().split())
answer = int(1e9)
q = deque([])
graph = []
dx, dy = [0,1,0,-1], [1,0,-1,0]
for _ in range(n) :
    graph.append(list(input()))

q.append((0,0,1))
visited = [[[0] * 2 for _ in range(m)] for __ in range(n)]
visited[0][0][1] = 1

def bfs() :
    while q:
        x,y,w = q.popleft()
        if (x, y) == (n-1, m-1) :
            return visited[x][y][w]

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if graph[nx][ny] == '1' and w == 1 : # 벽을 만났지만 벽을 뚫을 수 있는 상태다 
                    visited[nx][ny][0] = visited[x][y][1] + 1 # 벽을 뚫었으니 [nx][ny][0]을 [x][y][1]  + 1로 업데이트 
                    q.append((nx,ny,0))
                elif graph[nx][ny] == '0' and visited[nx][ny][w] == 0 : # 갈 수 있는 길이고 방문하지 않앗다면 이동
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx,ny,w))
    
    return -1
                
print(bfs())
