# https://www.acmicpc.net/problem/1005
import sys
input = sys.stdin.readline
from collections import deque
def topology() :
    dp = [0] * (n+1)
    q = deque()
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)
            dp[i] += lst[i]

    while q : 
        node = q.popleft()
        for i in graph[node] : 
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[node] + lst[i])
            if indegree[i] == 0 :
                q.append(i)
    return dp[target]


for _ in range(int(input())) :
    n, m = map(int, input().split())    
    lst = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1) 

    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b) 
        indegree[b] += 1

    target = int(input())

    print(topology())


