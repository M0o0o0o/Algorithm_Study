# https://www.acmicpc.net/problem/11265

n, m = map(int, input().split())
graph = [[]]

for _ in range(n) :
    graph.append([0] + list(map(int, input().split())))

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if i == j or i == k or j == k : continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(m) :
    a,b,c = map(int, input().split())
    if graph[a][b] <= c : 
        print('Enjoy other party')
    else :
        print('Stay here') 


