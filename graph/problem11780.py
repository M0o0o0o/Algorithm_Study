# https://www.acmicpc.net/problem/11780

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
root = [[[]] * (n+1) for _ in range(n+1)]

for i in range(1, n+1) :
    graph[i][i] = 0


for _ in range(m) :
    a,b,c = map(int,input().split())
    if graph[a][b] > c :
        graph[a][b] = c
        root[a][b] = [a,b]

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) : 
            if graph[i][j] > graph[i][k] + graph[k][j] :
                graph[i][j] = graph[i][k] + graph[k][j]
                root[i][j] = root[i][k] + root[k][j][1:]

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if graph[i][j] == INF :
            print('0', end = ' ')
        else :
            print(graph[i][j], end =' ')
    print()


for i in range(1,n+1) :
    for j in range(1, n+1) :
        if i ==j :
            print('0')
        else :
            print(len(root[i][j]), end = ' ')
            for r  in root[i][j] :
                print(r, end = ' ')
            print()