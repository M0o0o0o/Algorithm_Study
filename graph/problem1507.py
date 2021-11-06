# https://www.acmicpc.net/problem/1507

import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
graph = []
ans = 0
check = [[True] * n for _ in range(n)]
for _ in range(n) :
    graph.append(list(map(int,input().split())))

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if i == j or i == k or j == k : continue
            if graph[i][j] == graph[i][k] + graph[k][j] :
                check[i][j] = False
            if graph[i][j] > graph[i][k] + graph[k][j] :
                ans = -1

if ans != -1 :
    for i in range(n) :
        for j in range(n) :
            if check[i][j] :
                ans += graph[i][j]

print(ans // 2)
                






