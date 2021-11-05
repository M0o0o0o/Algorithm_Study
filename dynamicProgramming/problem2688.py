# https://www.acmicpc.net/problem/2688

import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    if n == 1 :
        print('10')
        continue
    dp = [[0] * 11 for _ in range(n+1)]
    dp[1] = [1,1,1,1,1,1,1,1,1,1,10]
    for i in range(2,n+1) :
        for j in range(11) :
            if j == 10 :
                dp[i][j] = sum(dp[i])
                continue
            if j == 0 :
                dp[i][0] = dp[i-1][10]
                continue
            dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

    print(dp[n][10])
    

