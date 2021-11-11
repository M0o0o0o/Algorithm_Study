# https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    coin = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money+1)
    dp[0] = 1

    for c in coin :
        for i in range(1, money + 1) :
            if i - c >= 0 :
                dp[i] += dp[i-c]
    print(dp[money])
            