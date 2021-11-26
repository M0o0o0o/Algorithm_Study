# https://www.acmicpc.net/problem/3109
import sys; input = sys.stdin.readline

def dfs(x,y) :
    if y == m-1 :
        return True
    for d in dx : 
        nx, ny = x + d, y + 1 
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == '.' :
            visited[nx][ny] = True
            if dfs(nx,ny) : return True
    return False            
            
    
n, m = map(int, input().split())
graph = []
dx = [-1,0,1]
ans = 0
visited = [[False] * (m) for _ in range(n)]
for _ in range(n) :
    graph.append(list(input().strip('\n')))
    
for i in range(n) :
    if not visited[i][0] and graph[i][0] == '.' : 
        visited[i][0] = True
        if dfs(i,0) : 
            ans += 1

        
print(ans)