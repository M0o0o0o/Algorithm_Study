# https://www.acmicpc.net/problem/2644

n = int(input()) + 1
x, y = map(int,input().split())
m = int(input())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for i in range(1, n) :
    graph[i][i] = 0
 
for _ in range(m) :
    a, b= map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n) :
    for i in range(1, n) :
        for j in range(1, n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[x][y] == INF :
    print(-1)
else :
    print(graph[x][y])