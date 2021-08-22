# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq
from collections import deque
def solution(operations):
    q = []
    for op in operations :
        op = op.split()
        if op[0] == "I" :
            heapq.heappush(q, int(op[1]))
            continue  
        if not q :
            continue
        if op[1] == "1" :
            buf = deque(q)
            buf.pop()
            q = list(buf)
            heapq.heapify(q)
        else :
            heapq.heappop(q)
    
    if not q : 
        return [0,0]
    queue = list(q)
    queue.sort()
    return [queue[len(queue)-1],queue[0]]




print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))