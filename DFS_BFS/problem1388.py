# https://www.acmicpc.net/problem/1388

n, m = map(int,input().split())
graph = []
for _ in range(n) :
    graph.append(list(input()))

answer = 0 

for i in range(n) :
    prev = '|'
    for j in range(m) :
        if graph[i][j] == '-' and graph[i][j] != prev :
            answer += 1
        prev = graph[i][j]

for j in range(m) :
    prev = '-'
    for i in range(n) :
        if graph[i][j] == '|' and graph[i][j] != prev :
            answer += 1
        prev = graph[i][j]
print(answer)