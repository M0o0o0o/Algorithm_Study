# https://www.acmicpc.net/problem/14503

n, m = map(int,input().split())
graph = []
x, y, d = map(int,input().split())

# 북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n) :
    graph.append(list(map(int,input().split())))
    
answer = 0

while True :
    check = False
    if graph[x][y] == 0 :
        graph[x][y] = 2
        answer += 1

    for _ in range(4) :
        d = (d-1) % 4 
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny 
            check = True 
            break
    if not check :
        nx = x - dx[d] 
        ny = y - dy[d] 
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 :
                print(answer)
                break
            else :
                x, y = nx, ny
        else :
            print(answer)
            break
    

