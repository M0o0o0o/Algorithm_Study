# https://www.acmicpc.net/problem/11781

import sys 
input = sys.stdin.readline
import heapq

n, m, s, e = map(int, input().split())  
graph = [[] for _ in range(n+1)]
INF = float('inf')
distance = [INF] * (n+1)

for _ in range(m) :
    a, b, l, t1, t2 = map(int, input().split())
    graph[a].append((b,l,t1))
    graph[b].append((a,l,t2))
    
q = []
heapq.heappush(q, (0,1))
distance[1] = 0 

while q : 
    dist, now = heapq.heappop(q)
    if distance[now] < dist  :
        continue
    for node, length, jam in graph[now] : 
        # 퇴근 시간 여부의 따른 cost 계산
        # 퇴근 시간이 아닐 때에는 거리 1 이동하는데 1분 
        # 퇴근 시간일 경우에는 거리 1 이동하는데 2분 
        cost = dist + length 
        if jam and ((dist <= s <= cost) or (dist <= e <= cost)):
            cost_ = 0 
            if dist <= s <= cost : 
                cost_ = cost - s 
            else : 
                cost_ = cost - e
            #cost_ = 3 
            length_ = cost_ / 2  
            #length_ = 1.5
            if length_ < length :  
                cost_ += length - length_  # 3 += (8 - )
            elif length_ > length: 
                cost_ -= (length_ - length) / 2
            cost = cost_ + dist
            if node ==2 : 
                print('test :', cost_, dist)                 
        if cost < distance[node] : 
            distance[node] = cost 
            heapq.heappush(q,(cost, node))
            

print(distance)
