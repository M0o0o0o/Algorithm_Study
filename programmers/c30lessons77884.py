# https://programmers.co.kr/learn/courses/30/lessons/77884

import sys
input = sys.stdin.readline

lst = [0] * (1001)

for num in range(1, 1001):
    n = num
    while n <= 1000:
        lst[n] += 1
        n += num


def solution(left, right):
    ans = 0
    for num in range(left, right+1, +1):
        if lst[num] % 2 == 0:
            ans += num
            continue
        ans -= num
    return ans


print(solution(13, 17))
