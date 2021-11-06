# https://www.acmicpc.net/problem/13424

import sys 
input = sys.stdin.readline
INF = int(1e9)
for _ in range(int(input())) :
    ans, lst = INF, []
    n, m = map(int, input().split())
    
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1) :
        graph[i][i] = 0

    for _ in range(m) :
        a, b, c = map(int, input().split())
        graph[a][b], graph[b][a] = c, c

    for k in range(1,n+1) :
        for i in range(1,n+1) :
            for j in range(1,n+1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 
    
    k = int(input())
    friend = list(map(int, input().split()))

    for i in range(1, n+1) :
        cost = 0
        for f in friend : 
            cost += graph[f][i]

        if ans > cost :
            ans = cost 
            lst = [i]
        if ans == cost : 
            lst.append(i)
    
    lst.sort()
    print(lst[0])
