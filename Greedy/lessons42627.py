# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    jobs.sort()
    answer = 0
    clock = 0
    count = 0
    q = []
    while count < len(jobs) :
        for i in range(len(jobs)) :
            arrive, work = jobs[i] 
            if arrive <= clock and  arrive != -1:
                heapq.heappush(q, (work, arrive))
                jobs[i] = [-1,-1]
        if not q :
            clock += 1
            continue
        
        work, arrive = heapq.heappop(q) 
        count += 1
        answer += (clock-arrive) + work
        clock += work
    return answer // len(jobs)

