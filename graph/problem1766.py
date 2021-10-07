# https://www.acmicpc.net/problem/1766

import heapq

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indgree = [0] * (n+1)
q = []

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b) 
    indgree[b] += 1

for i in range(1,n+1) :
    if indgree[i] == 0 :
        heapq.heappush(q, i)

while q : 
    node = heapq.heappop(q)
    print(node, end = ' ')

    for i in graph[node] :
        indgree[i] -= 1
        if indgree[i] == 0 :
            heapq.heappush(q,i)
