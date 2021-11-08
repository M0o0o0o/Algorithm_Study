import sys
sys.setrecursionlimit(10**5)

def dfs(node) :
    global ans
    visited[node] = True
    cycle.append(node)
    next_node = lst[node] 

    if visited[next_node] :
        if next_node in cycle :
            ans += cycle[cycle.index(next_node):]
        return
    else :
        dfs(next_node)


for _ in range(int(input())) :
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    ans = []
    visited = [False] + [False] * n

    for i in range(1, n+1) :
        if not visited[i] :
            cycle = []
            dfs(i)

    print(n - len(ans))