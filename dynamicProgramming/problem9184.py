# https://solutionsolutionsolution.acmicpc.net/problem/9184


from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)


def solution(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if dp[(a, b, c)] != 0:
        return dp[(a, b, c)]
    if a > 20 or b > 20 or c > 20:
        dp[(a, b, c)] = solution(20, 20, 20)
    elif a < b and b < c:
        dp[(a, b, c)] = solution(a, b, c-1) + \
            solution(a, b-1, c-1) - solution(a, b-1, c)
    else:
        dp[(a, b, c)] = solution(a-1, b, c) + solution(a-1, b-1, c) + \
            solution(a-1, b, c-1) - solution(a-1, b-1, c-1)
    return dp[(a, b, c)]


dp = defaultdict(int)
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    ans = solution(a, b, c)
    print('w(' + str(a) + ', ' + str(b) + ', ' + str(c) + ') =', ans)
