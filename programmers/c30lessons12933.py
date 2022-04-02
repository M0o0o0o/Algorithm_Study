# https://programmers.co.kr/learn/courses/30/lessons/12933


def solution(n):
    lst = list(str(n))
    lst.sort(reverse=True)
    return int("".join(lst))


print(solution(118372))
print(solution(1100008))
