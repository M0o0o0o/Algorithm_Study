# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    return sum([num for num in range(min(a, b), max(a, b) + 1)])


print(solution(3, 5))
