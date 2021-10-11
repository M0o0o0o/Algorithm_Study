# https://www.acmicpc.net/problem/1939

from collections import deque

def bfs(value) : 
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True

    while q : 
        a = q.popleft()
        
        for b, cost in graph[a] :
            if cost >= value and not visited[b] : 
                q.append(b)
                visited[b] = True

    if not visited[end] :
        return False
    return True
            


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

low, high = int(1e9), -1
for _ in range(m) :
    a,b,c = map(int,input().split())
    low, high = min(low, c), max(high, c)
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int,input().split())


while not low > high :
    mid = (low+high) // 2

    if bfs(mid) :
        low = mid + 1 
    else :
        high = mid - 1

print(high)