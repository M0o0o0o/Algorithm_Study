# https://www.acmicpc.net/problem/14495

import sys
sys.setrecursionlimit(10**5)


def recur(num):
    if dp[num] != -1:
        return dp[num]
    dp[num] = recur(num-1) + recur(num-3)
    return dp[num]


n = int(input())

dp = [-1] * 117
dp[1], dp[2], dp[3] = 1, 1, 1
print(recur(n))
