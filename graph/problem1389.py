# https://www.acmicpc.net/problem/1389

n, m = map(int,input().split())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for _ in range(m) :
    a, b = map(int,input().split())
    a-=1
    b-=1
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n) :
    graph[i][i] = 0

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
total = INF
for i in range(n) :
    if total > sum(graph[i]) :
        total, answer = sum(graph[i]), i + 1
    
print(answer)