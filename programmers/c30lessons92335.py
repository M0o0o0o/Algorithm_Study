# https://programmers.co.kr/learn/courses/30/lessons/92335

from math import sqrt


def convert(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1]


def solution(n, k):
    ans = 0
    for num in list(convert(n, k).split('0')):
        if num == '':
            continue
        num = int(num)
        if num == 1:
            continue
        flag = True
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                flag = False
                break
        if flag:
            ans += 1
    return ans


print(solution(437674, 3))
print(solution(110011, 10))
