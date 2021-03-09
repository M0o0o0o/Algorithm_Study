# 백준 2606

from collections import deque


def bfs(graph, start, visited) :
    queue = deque([start])

    visited[start] = True
    while queue : 
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] : 
                queue.append(i)
                visited[i] = True



comCount = int(input())
pair = int(input())
graph = [[] for _ in range(comCount+1)]

for _ in range(pair) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (comCount+1)

bfs(graph, 1, visited) 

answer = 0
for i in visited :
    if i :
        answer += 1
print(answer-1)
