# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []

    while progresses :
        count = 0 
        for p in progresses :
            if p >= 100 :
                count += 1
            else  :
                break

        for i in range(count) :
            progresses.pop(0)
            speeds.pop(0)
            
        if count > 0 :
            answer.append(count)
        length = len(progresses)
 
        for i in range(length) :
            p = progresses.pop(0)
            progresses.append(p + speeds[i])

    return answer

print(solution([93, 30, 55],[1, 30, 5]))