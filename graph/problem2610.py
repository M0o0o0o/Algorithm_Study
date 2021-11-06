# https://www.acmicpc.net/problem/2610
import sys 
input = sys.stdin.readline
n, m = int(input()), int(input())
INF = int(1e9)
graph =[[INF] * (n+1) for _ in range(n+1)]
group = []

for i in range(1,n+1) :
    graph[i][i] = 0

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1


for k in range(1, n+1) :
    for  i in range(1,n+1) :
        for j in range(1,n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        flag = True
        for g in range(len(group)) :
            if graph[i][j] != INF and (i in group[g] or j in group[g]) :
                flag = False
                group[g].add(i)
                group[g].add(j)
                break
        if flag and graph[i][j] != INF :
            group.append(set([i,j]))           

print(len(group))
answer = []

for g in group :
    lst = list(g)
    min_cost,  min_mamber= INF, 0

    for c in lst :
        cost = -1
        for m in lst :
            cost = max(cost, graph[m][c])
        if min_cost > cost :
            min_cost = cost
            min_member = c
             
    answer.append(min_member)

answer.sort()
for a in answer :
    print(a)      

