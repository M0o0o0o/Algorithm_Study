# https://www.acmicpc.net/problem/17142
from itertools import combinations
from collections import deque

def bfs(select) :
    visited = [[0] * n for _ in range(n)]
    q = deque()
    for x,y in select :
        q.append((x,y))
        visited[x][y] = 1

    while q : 
        x, y = q.popleft()
        flag = False
        count = 0
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] in [0,2]  :
                if graph[nx][ny] == 0 : flag = True
                visited[nx][ny] = visited[x][y] + 1
                count += 1
                q.append((nx,ny))

        if not flag : 
            for _ in range(len(q) - count, len(q)) :
                visited[nx][ny] -= 1 

    time = 0
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == 0 and graph[i][j] in [0,2] :
                return int(1e9)
            time = max(time, visited[i][j])
    return time -1

n, m = map(int,input().split())
graph = []
virus = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = int(1e9)
for i in range(n) :
    graph.append(list(map(int,input().split())))
    for j in range(n) :
        if graph[i][j] == 2 :
            virus.append((i,j))

lst = list(combinations(virus, m))
for i in range(len(lst)) :
    answer = min(bfs(lst[i]), answer)

if answer < int(1e9) :
    print(answer)
else :
    print(-1)