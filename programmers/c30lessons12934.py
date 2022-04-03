# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    num = 1
    while True:
        if num ** 2 > n:
            break
        if num ** 2 == n:
            return (num + 1) ** 2
        num += 1
    return -1


print(solution(121))
print(solution(3))
