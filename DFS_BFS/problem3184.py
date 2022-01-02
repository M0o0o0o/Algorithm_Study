# https://www.acmicpc.net/problem/3184
from collections import deque

def bfs(i,j) : 
    global wolf, sheep, farm
    w, s  = 0, 0 
    q = deque([(i, j)])
    if farm[i][j] == 'o' : s += 1
    elif farm[i][j] == 'v' : w += 1
    farm[i][j] = '#'
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m : 
                if farm[nx][ny] != '#' :
                    if farm[nx][ny] == 'o' : s += 1
                    elif farm[nx][ny] == 'v' : 
                        w += 1
                    farm[nx][ny] = '#'
                    q.append((nx,ny))
    if s > w : 
        sheep += s 
    else : 
        wolf += w
n, m = map(int, input().split())
dx, dy = [0,1,0,-1], [1,0,-1,0]
farm = []
sheep, wolf = 0, 0
for _ in range(n) :
    farm.append(list(input()))
    
for i in range(n) :
    for j in range(m) :
        if farm[i][j] != '#' : 
            bfs(i, j)

print(sheep, wolf)

