# https://www.acmicpc.net/problem/1948
from collections import deque
import sys 
input = sys.stdin.readline
n, m = int(input()), int(input())

graph = [[] * (n+1) for _ in range(n+1)]
back_graph = [[] * (n+1) for _ in range(n+1)]

indegree = [0] * (n+1) 
ans = [0] * (n+1)
check = [0] * (n+1)

q = deque()

for _ in range(m) :
    a,b,c, = map(int, input().split())
    graph[a].append((b,c))
    back_graph[b].append((a,c))
    indegree[b] += 1
    
s, e = map(int ,input().split())

q.append(s)

while q :
    now = q.popleft()
    for n, c in graph[now] :
        indegree[n] -= 1
        ans[n] = max(ans[n], ans[now] + c)
        if indegree[n] == 0 :
            q.append(n)

cnt = 0
q.append(e)
while q :
    now = q.popleft()
    for n, t in back_graph[now] :
        if ans[now] - ans[n] == t :
            cnt += 1
            if check[n] == 0 :
                q.append(n) 
                check[n] = 1
                
print(ans[e])
print(cnt)        