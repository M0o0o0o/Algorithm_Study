# https://www.acmicpc.net/problem/1976
n, m = int(input()), int(input())
graph =[]
for _ in range(n) :
    graph.append(list(map(int, input().split())))
root = list(map(int, input().split()))

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 0 and i != j : graph[i][j] = int(1e90)

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 'YES'
for i in range(1, len(root)) :
    if graph[root[i-1]-1][root[i]-1] >= int(1e9) :
        result = 'NO' 
        break
print(result)   
        