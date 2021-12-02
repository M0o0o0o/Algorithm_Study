import sys
import heapq
input = sys.stdin.readline

def djikstra(start) :
    q = []
    heapq.heappush(q, (0,start,0))
    distance[0][0] = 0

    while q :
        dist, now, mode = heapq.heappop(q)
        if distance[now][mode] < dist : continue
        for node, dist2 in graph[now] :
            cost = dist + dist2
            if distance[node][mode] > cost :
                heapq.heappush(q, (cost, node, mode))
                distance[node][mode] = cost

            if mode == 0 and plist[node] and distance[node][1] > cost :
                heapq.heappush(q, (cost, node, 1))
                distance[node][1] = cost

INF = float("inf")
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[INF for _ in range(2)] for _ in range(n+1)]

for _ in range(m) :
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s, e = map(int, input().split())
p = int(input())
plist = [False for _ in range(n+1)]
pbuf = list(map(int, input().split()))

for p in pbuf :
    plist[p] = True

djikstra(s)

if distance[e][1] != INF :
    print(distance[e][1])
else :
    print(-1)

