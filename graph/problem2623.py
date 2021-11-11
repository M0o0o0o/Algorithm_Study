# https://www.acmicpc.net/problem/2623
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indgree = [0] * (n+1)
ans = []

for _ in range(m) :
    lst = list(map(int, input().split()))
    for i in range(2, len(lst)) :
        graph[lst[i-1]].append(lst[i])
        indgree[lst[i]] += 1
        
q = deque()
for i in range(1,n+1) :
    if indgree[i] == 0 :
        q.append(i)

while q : 
    now = q.popleft()
    ans.append(now)
    
    for i in graph[now] :
        indgree[i] -= 1
        if indgree[i] == 0 :
            q.append(i)

if len(ans) == n :
    for a in ans :
        print(a)
else :
    print(0)
    