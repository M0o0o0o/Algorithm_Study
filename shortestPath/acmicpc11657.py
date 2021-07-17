# https://www.acmicpc.net/problem/11657
# 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우,
# C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.
# 1번 도시에서 출발해서 다른 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
cycle = False
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b, w = map(int,input().split())
    graph[a].append((b,w))

distance = [INF] * (n+1)
distance[1] = 0
for i in range(1, n+1) :
    for j in range(1, n+1) :
        for node in graph[j] :
            if distance[j] != INF and distance[node[0]] > node[1] + distance[j] :
                distance[node[0]] = node[1] + distance[j]
                if i == n :
                    cycle = True
                    break


if cycle :
    print('-1')
else :
    for i in range(2, n+1) :
        if distance[i] == INF : 
            print('-1')
        else :
            print(distance[i])

    