# https://www.acmicpc.net/problem/2252

from collections import deque

n, m = map(int,input().split())
answer = []
graph = [[] for _ in range(n+1)]
indgree = [0] * (n+1)

for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    indgree[b] += 1

q = deque()
for i in range(1, n+1) :
    if indgree[i] == 0 :
        q.append(i)

while q : 
    node = q.popleft()
    answer.append(node)

    for i in graph[node] :
        indgree[i] -= 1
        if indgree[i] == 0 :
            q.append(i)

for i in answer : 
    print(i, end=' ')
