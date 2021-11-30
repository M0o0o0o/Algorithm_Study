# https://www.acmicpc.net/problem/23793
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, graph) :
    distance = [float("inf")] * (n+1) 
    distance[start] = 0
    q = [(0,start)]

    while q :
        dist, now = heapq.heappop(q)
        
        if dist > distance[now] : continue
        
        for node, node_cost in graph[now] : 
            cost = distance[now] + node_cost
            if distance[node] >= cost : 
                distance[node] = cost 
                heapq.heappush(q, (cost, node))
    
    return distance

n, m = map(int, input().split())

graph1= [[] for _ in range(n+1)]
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph1[a].append((b,c))
    
x,y,z = map(int, input().split())

graph2 = [[] for _ in range(n+1)]
for i in range(n+1) :
    for b, c in graph1[i] : 
        if i == y or b == y : 
            continue
        graph2[i].append((b,c))
        
d1 = dijkstra(x, graph1)
d2 = dijkstra(y, graph1)
d3 = dijkstra(x, graph2)

print(d1[y] + d2[z] if d1[y] + d2[z] != float("inf") else -1, d3[z] if d3[z] != float("inf") else -1)

