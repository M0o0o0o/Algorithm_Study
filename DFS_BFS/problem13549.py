# https://www.acmicpc.net/problem/13549
from collections import deque

n, k = map(int,input().split())
visited = [0] * 100001

visited[n] = 1
q = deque([n])

while q : 
    x = q.popleft()
    if x == k :
        print(visited[x] - 1)
        break
    
    if x * 2 <= 100000 and visited[x*2] == 0 :
        q.append(x*2)
        visited[x*2] = visited[x]

    if x-1 >= 0 and visited[x-1] == 0 :
        q.append(x-1)
        visited[x-1] = visited[x] + 1

    if x+1 <= 100000 and visited[x+1] == 0 :
        q.append(x+1)
        visited[x+1] = visited[x] + 1
        
