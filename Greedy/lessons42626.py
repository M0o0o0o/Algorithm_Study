# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K) :
    answer = 0
    q = []
    for i in scoville :
        heapq.heappush(q, i)
    while True :
        num = heapq.heappop(q)
        if num > K :
            return answer
        if not q :
            return -1
        two = heapq.heappop(q)
        heapq.heappush(q, num + (two*2)) 
        answer+=1

print(solution([1, 2, 3, 9, 10, 12],7))