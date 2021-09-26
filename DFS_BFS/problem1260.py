# https://www.acmicpc.net/problem/1260
from collections import deque
n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b) 
    graph[b].append(a) 

for i in range(1,n+1) :
    graph[i].sort()

def dfs(node, count) :
    visited[node] = True
    print(node, end = ' ')
    if count == n : 
        return True
    for i in graph[node] : 
        if not visited[i] : 
            if dfs(i, count + 1) :
                return

dfs(v, 1)  
print()
visited = [False] * (n+1)

q = deque([])
q.append(v)
visited[v] = True
count = 0
while  q : 
    node = q.popleft()
    print(node, end = ' ')
    count += 1
    if count == n :
        break
    for i in graph[node] :
        if not visited[i] :
            q.append(i)
            visited[i] = True



