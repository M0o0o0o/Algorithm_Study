# https://www.acmicpc.net/problem/1655

import heapq
import sys
input = sys.stdin.readline

leftq, rightq = [], []
for _ in range(int(input())) :
    num = int(input())
    if len(leftq) == len(rightq) :
        heapq.heappush(leftq, -num)
    else :
        heapq.heappush(rightq, num)
    if rightq and (-leftq[0] > rightq[0]) :
        heapq.heappush(rightq, -heapq.heappop(leftq))
        heapq.heappush(leftq, -heapq.heappop(rightq))
        
    print(-leftq[0])
