# https://www.acmicpc.net/problem/9461

for _ in range(int(input())) :
    n = int(input())
    dp = [0] * n

    for i in range(n) :
        if (i-2) >= 0 and (i-3) >= 0 :
            dp[i] = dp[i-2] + dp[i-3]
        else :
            dp[i] = 1
    
    print(dp[n-1])
