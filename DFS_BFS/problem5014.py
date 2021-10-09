# https://www.acmicpc.net/problem/5014

from collections import deque

n, start, target, up, down = map(int,input().split())

visited = [-1] * (n+1)
visited[start] = 0 
q = deque([start])

while q : 
    s = q.popleft()
    if s == target : 
        break
    
    if s + up <= n and visited[s+up] == -1 :
        visited[s+up] = visited[s] + 1 
        q.append(s+up)
    
    if s - down >= 1 and visited[s-down] == -1 :
        visited[s-down] = visited[s] + 1
        q.append(s-down)
    
if visited[target] == -1 :
    print('use the stairs')
else :
    print(visited[target])