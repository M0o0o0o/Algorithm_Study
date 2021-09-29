# https://www.acmicpc.net/problem/10451

import sys
sys.setrecursionlimit(2000)

def dfs(node) :
    visited[node] = True
    if not visited[lst[node]] :
        dfs(lst[node]) 


for _ in range(int(input())) :
    n = int(input())
    lst = [0] + list(map(int,input().split()))
    answer = 0
    visited = [False] * (n+1) 

    for i in range(1, n+1) :
        if not visited[i] :
            dfs(i)
            answer += 1
    print(answer)

