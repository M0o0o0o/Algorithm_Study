# https://www.acmicpc.net/problem/9370

# s 지점에서 출발 (다익스트라)
# 목적지 후보들 중 하나의 목적지
# 우회하지 않고 최단거리로 갈 것이라 확신한다(최단경로 문제)
# g와 h 사이에 있는 도로를 지나갔다는 것을 알아냈다. 

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph) :
    distance = [INF] * len(graph)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

# 다익스트라 3번 
# for _ in range(int(input())) :
#     n, m ,t = map(int,input().split()) #각각 교차로, 도로, 목적지 후보의 개수 
#     s, g, h = map(int, input().split()) # 출발지, 듀오의 지나간 교차로 정보 
#     graph = [[] for _ in range(n+1)]
#     target = []
#     answer = [] 
#     for _ in range(m) :
#         a, b, d = map(int,input().split())
#         graph[a].append((b,d))
#         graph[b].append((a,d))

#     for _ in range(t) :
#         target.append(int(input()))

#     distance = dijkstra(s, graph)
#     distanceG = dijkstra(g, graph)
#     distanceH = dijkstra(h, graph)

#     for t in target :
#         sght = distance[g] + distanceG[h] + distanceH[t]
#         shgt  = distance[h] + distanceH[g] + distanceG[t]
#         if sght == distance[t] or shgt == distance[t] :
#             answer.append(t)

    
#     answer.sort()
#     for a in answer :
#         print(a, end =' ')


# 다익스트라 2번 
# for _ in range(int(input())) :
#     n, m ,t = map(int,input().split()) #각각 교차로, 도로, 목적지 후보의 개수 
#     s, g, h = map(int, input().split()) # 출발지, 듀오의 지나간 교차로 정보 
#     graph = [[] for _ in range(n+1)]
#     target = []
#     answer = [] 
#     weight = 0
#     for _ in range(m) :
#         a, b, d = map(int,input().split())
#         if (a == g and b == h)  or (b == g and a == h) :
#             weight = d
#         graph[a].append((b,d))
#         graph[b].append((a,d))

#     for _ in range(t) :
#         target.append(int(input()))

#     distance = dijkstra(s, graph)
#     smallDist = 0
#     bigDist = 0 

#     if distance[g] > distance[h] :
#         bigDist = g
#         smallDist = h
    
#     else :
#         bigDist = h
#         smallDist  = g
    
#     distance2 = dijkstra(bigDist, graph)

#     for t in target :
#         dist = distance[smallDist] + weight + distance2[t]

#         if dist == distance[t] :
#             answer.append(t)
    
#     answer.sort()
#     for a in answer :
#         print(a, end =' ')


# 다익스트라 한번 
for _ in range(int(input())) :
    n, m ,t = map(int,input().split()) #각각 교차로, 도로, 목적지 후보의 개수 
    s, g, h = map(int, input().split()) # 출발지, 듀오의 지나간 교차로 정보 
    graph = [[] for _ in range(n+1)]
    target = []
    answer = [] 
    weight = 0
    for _ in range(m) :
        a, b, d = map(int,input().split())
        if (a == g and b == h)  or (b == g and a == h) :
            graph[a].append((b,d*2-1))
            graph[b].append((a,d*2-1))

        else :
            graph[a].append((b,d*2))
            graph[b].append((a,d*2))

    for _ in range(t) :
        target.append(int(input()))

    distance = dijkstra(s, graph)


    for t in target :
        if distance[t] % 2 != 0 :
            answer.append(t)
    
    answer.sort()
    for a in answer :
        print(a, end =' ')