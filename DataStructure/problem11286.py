# https://www.acmicpc.net/problem/11286

import heapq 
import math
import sys 
input = sys.stdin.readline
n = int(input())
q = []

for _ in range(n) :
    num = int(input())
    if num == 0 :
        if not q : print(0)
        else : 
            absNum, num = heapq.heappop(q)
            while q :
                a, b = heapq.heappop(q) 
                if a == absNum and num > b : 
                    heapq.heappush(q, (absNum, num))
                    absNum, num = a, b
                else : 
                    heapq.heappush(q, (a,b))
                    break
            print(num)
        continue 

    heapq.heappush(q, (abs(num), num))