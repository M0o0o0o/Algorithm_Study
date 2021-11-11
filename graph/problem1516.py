# https://www.acmicpc.net/problem/1516

import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
indgree = [0]  * (n+1) 
graph = [[] for i in range(n+1)]
value = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1) :
    buf = list(map(int, input().split()))
    value[i] = buf[0]
    for j in buf[1:] :
        if j == -1 : continue
        graph[j].append(i) 
        indgree[i] += 1

q = deque()

for i in range(1,n+1) :
    if indgree[i] == 0 :
        dp[i] = value[i]
        q.append(i)
        
while q :
    now = q.popleft()
    for i in graph[now] :
        indgree[i] -= 1
        dp[i] = max(dp[i], value[i] + dp[now])
        if indgree[i] == 0 :
            q.append(i)
        
for i in dp[1:] :
    print(i)
