# https://www.acmicpc.net/problem/2133

n = int(input())

dp = [0] * (n+1) 
dp[0] = 1
if n >= 2 : dp[2] = 3
if n >= 4 : dp[4] = 11

for i in range(1, n+1) :
    if i % 2 == 0 and i != 2 and i != 4:
        dp[i] += (dp[i-2]) * 3

        for j in range(i-4, -1, -2) :
            dp[i] += (dp[j] * 2) 

if n % 2 == 0 :
    print(dp[n])
else :
    print(0)