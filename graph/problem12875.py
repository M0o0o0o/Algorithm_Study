import sys
input = sys.stdin.readline

n, d = int(input()), int(input())
graph = []
INF = int(1e9)

for i in range(n) :
    lst = list(input().strip('\n'))
    for j in range(n) :
        if i == j  : lst[j] = 0 
        elif lst[j] == 'Y' : lst[j] = 1
        else : lst[j] = INF
    graph.append(lst)
    
for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
big = 0
for i in range(n) :
    for j in range(n) :
        if i != j : big = max(big, graph[i][j])
        
if big != INF :
    print(big * d) 
else :
    print(-1)