# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    return [int(s) for s in list(str(n)[::-1])]


print(solution(12345))
