# https://www.acmicpc.net/problem/17144
import sys
input = sys.stdin.readline

def dirty() : 
    lst = [] 
    for i in range(n) :
        for j in range(m) : 
            if graph[i][j] > 0 :
                lst.append((i,j, graph[i][j]))
    for x, y, value in lst : 
        count = 0
        for i in range(0, 4) : 
            nx, ny = x + dx[i], y + dy[i]   
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != -1:
                graph[nx][ny] += (value // 5)
                count += 1
        graph[x][y] -=  (value // 5) * count

def initialClean(air, dx, dy, clean) :
    x, y = air  
    for i in range(4) : 
        while True : 
            x, y = x + dx[i], y + dy[i]
            if 0 <= x < n and 0 <= y < m and graph[x][y] != -1: 
                clean.append((x,y))
            else : 
                x, y = x - dx[i], y - dy[i]
                break
            
n, m, t = map(int, input().split())
graph = []
airup, airdown = 0, 0
dx, dy = [0,1,0,-1], [1,0,-1,0]
upx, upy = [0,-1,0,1], [1,0,-1,0]
upclean, downclean = [], []

for i in range(n) :
    graph.append(list(map(int, input().split())))
    for j in range(m) :
        if graph[i][j] == -1 : 
            if airup == 0 : 
                airup = (i,j)
            else : 
                airdown = (i,j)

initialClean(airup, upx, upy, upclean)
initialClean(airdown, dx,dy, downclean)
upclean = upclean[::-1]
downclean = downclean[::-1]

for _ in range(t) :
    dirty()
    for i in range(1, len(upclean)) : 
        px,py = upclean[i-1]
        cx, cy = upclean[i]
        graph[px][py] = graph[cx][cy]
    for i in range(1, len(downclean)) : 
        px,py = downclean[i-1]
        cx, cy = downclean[i]
        graph[px][py] = graph[cx][cy]       
    graph[upclean[-1][0]][upclean[-1][1]] = 0
    graph[downclean[-1][0]][downclean[-1][1]] = 0
    

ans = [sum(graph[i]) for i in range(n)]
print(sum(ans) + 2)