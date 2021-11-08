# https://www.acmicpc.net/problem/21940

import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


friend = int(input())
friends = list(map(int,input().split()))
ans, ans_index = INF, []

for i in range(1,n+1) :
    cost = 0
    for f in friends :
        if graph[i][f] == INF or graph[f][i] == INF :
            cost = 0
            break
        cost = max(cost, graph[i][f] + graph[f][i])
    
    if ans > cost :
        ans = cost 
        ans_index = [i]
    elif ans == cost :
        ans_index.append(i)

for i in sorted(ans_index) :
    print(i, end = ' ')

