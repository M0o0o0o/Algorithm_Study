# https://www.acmicpc.net/problem/2210

def dfs(x,y,c) :
    if len(c) == 6 :
        result.add(c)
        return
    
    for i in range(4) :
        nx, ny = x + dx[i] , y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 : 
            dfs(nx,ny,c + graph[nx][ny])




graph = []
dx,dy = [0,1,0,-1], [1,0,-1,0]
for _ in range(5) :
    graph.append(list(input().split()))

result = set()

for i in range(5) :
    for j in range(5) :
        dfs(i,j,graph[i][j])


print(len(result))