# https://www.acmicpc.net/problem/9507

import sys
input = sys.stdin.readline


def recur(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = recur(n-1) + recur(n-2) + recur(n-3) + recur(n-4)
    return dp[n]


dp = [0] * 68
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4

for _ in range(int(input())):
    print(recur(int(input())))
