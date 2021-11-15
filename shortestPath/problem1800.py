# https://www.acmicpc.net/problem/1800
# 결정문제로 바꿔서 이분탐색 + 다익스트라로 풀이

import sys 
import heapq
input = sys.stdin.readline
INF = int(1e15)

def dijkstra(limit) :
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0,1))
    distance[1] = 0
    
    while q :
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist :
            continue
        
        for new, _dist in graph[now] :
            if _dist > limit :
                if dist + 1 < distance[new] :
                    distance[new] = dist + 1
                    heapq.heappush(q, (dist +1, new))
            else :
                if dist < distance[new] : 
                    distance[new] = dist 
                    heapq.heappush(q,(dist, new))
                    
    if distance[n] >  k :
        return False
    else :
        return True                

n, p, k = map(int, input().split())
graph =[[] for _ in range(n+1)]

for _ in range(p) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
l, r = 0, 1000001
ans = INF 

while l <= r :
    m = (l + r) // 2
    if dijkstra(m) :
        r = m - 1
        ans = m
    else :
        l = m + 1
        
if ans == INF :
    print(-1)
else :
    print(ans)