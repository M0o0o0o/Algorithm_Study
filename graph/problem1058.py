# https://www.acmicpc.net/problem/1058

import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    graph[i][i] = 0

for i in range(1,n+1) :
    lst = list(input().strip('\n'))
    for l in range(len(lst)) :
        if lst[l] == 'Y' :
            graph[i][l+1] = 1
            graph[l+1][i] = 1

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
result = 0
for i in range(1, n+1) :
    result = max(result, graph[i][1:].count(1) + graph[i][1:].count(2))

print(result)


