# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(department, budget):
    cnt = 0
    for d in sorted(department):
        if budget >= d:
            budget -= d
            cnt += 1
    return cnt


print(solution([1, 3, 2, 5, 4],	9))
print(solution([2, 2, 3, 3], 10))
