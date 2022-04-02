# https://programmers.co.kr/learn/courses/30/lessons/12922


def solution(n):
    return ("수박" * (n // 2)) + ("수" if n % 2 == 1 else "")


print(solution(3))
print(solution(1))
print(solution(2))
print(solution(4))
