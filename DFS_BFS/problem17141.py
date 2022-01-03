# https://www.acmicpc.net/problem/17141

import sys 
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def bfs(lst, graph2) :
    for i in range(n) :
        for j in range(n) :
            if graph2[i][j] == 0 and (i,j) not in lst : 
                graph2[i][j] = int(1e9)
    q = deque(lst)

    while q : 
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph2[nx][ny] != -1 : 
                if graph2[x][y] + 1 < graph2[nx][ny] : 
                    graph2[nx][ny] = graph2[x][y] + 1
                    q.append((nx,ny))
    
    value = 0
    for i in range(n) :
        value = max(value, max(graph2[i]))
    return value


n, m = map(int, input().split())
graph = []
virus = []
dx, dy = [0,1,0,-1], [1,0,-1,0]
ans = int(1e9)
for i in range(n) :
    graph.append(list(map(int, input().split())))
    for j in range(n) :
        if graph[i][j] == 1 :
            graph[i][j] = -1
        elif graph[i][j] == 2 : 
            virus.append((i,j))
            graph[i][j] = 0
        else : 
            graph[i][j] = int(1e9) 

for l in list(combinations(virus, m)) :
    ans = min(ans, bfs(list(l), copy.deepcopy(graph)))

if ans == int(1e9) : 
    print(-1)
else :
    print(ans)