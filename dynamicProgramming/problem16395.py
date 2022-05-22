# https://www.acmicpc.net/problem/16395

import sys
sys.setrecursionlimit(10**5)


def solution(r, c):
    global dp
    if c < 0 or c > r:
        return 0
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = solution(r-1, c-1) + solution(r-1, c)
    return dp[r][c]


n, k = map(int, input().split())
n, k = n-1, k-1
dp = [[-1] * (i+1) for i in range(31)]
dp[0][0], dp[1][0], dp[1][1] = 1, 1, 1

print(solution(n, k))
