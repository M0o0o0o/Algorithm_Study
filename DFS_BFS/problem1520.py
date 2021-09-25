# https://www.acmicpc.net/problem/1520

n, m = map(int,input().split())
answer = 0
graph = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dp = [[-1] * m for _ in range(n)]
for _ in range(n) :
    graph.append(list(map(int,input().split())))

def dfs(x,y) :
    if (x,y) == (n-1, m-1) :
        return 1
    if dp[x][y] != -1 :
        return dp[x][y]
    dp[x][y] = 0 
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m  and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx,ny) 
    return dp[x][y]

print(dfs(0,0))