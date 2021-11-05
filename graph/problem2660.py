# https://www.acmicpc.net/problem/2660

import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
score_lst = [[] for _ in range(n+1)]
for i in range(1,n+1) :
    graph[i][i] = 0

while True :
    a, b = map(int, input().split())
    if a + b == -2 : break
    graph[a][b] = 1
    graph[b][a] = 1 
    
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
                if i == j : continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

score = INF
for i in range(1, n+1) :
    _score = 0
    for j in range(1,n+1) :
        if graph[i][j] not in [INF, 0] :
            _score = max(_score, graph[i][j])
    score_lst[_score].append(i)
    score = min(score, _score)

print(score, len(score_lst[score]))
score_lst[score].sort()
for s in score_lst[score] :
    print(s, end = ' ')


