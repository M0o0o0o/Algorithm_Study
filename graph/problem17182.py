# https://www.acmicpc.net/problem/17182

import sys
import itertools
input = sys.stdin.readline

INF = int(1e9)
n, s = map(int, input().split())
graph = []

for _ in range(n) :
    graph.append(list(map(int,input().split())))

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

permu = [i for i in range(n) if i != s]
permu = list(itertools.permutations(permu, n-1))
ans = INF 

for i in range(len(permu)) :
    lst = list(permu[i])
    cost = 0
    for i in range(len(lst)) :
        if i == 0 :
            cost += graph[s][lst[i]]
        else :
            cost += graph[lst[i-1]][lst[i]]
        if cost > ans :
            break
    ans = min(ans, cost)

print(ans)