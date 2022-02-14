# https://www.acmicpc.net/problem/1325

from collections import deque

def bfs(start) : 
    global ans, ans_list
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    count = 1
    while q : 
        com = q.popleft()
        for node in graph[com] : 
            if not visited[node] : 
                visited[node] = True
                count += 1
                q.append(node) 
                
    if count == ans :
        ans_list.append(start)
    elif count > ans : 
        ans = count
        ans_list = [start]         


n, m = map(int, input().split())
ans = 0
ans_list = []
graph = [[] for _ in range(n+1)]

for _ in range(m) : 
    a, b = map(int, input().split())
    graph[b].append(a)
    
for i in range(1, n+1) : 
    bfs(i)
ans_list.sort()
    
print(*ans_list)