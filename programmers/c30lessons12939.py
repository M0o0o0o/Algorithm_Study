# https://programmers.co.kr/learn/courses/30/lessons/12939


def solution(s):
    lst = list(map(int, s.split(' ')))
    return str(min(lst)) + " " + str(max(lst))


print(solution("-1 -2 -3 -4"))
