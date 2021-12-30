# https://www.acmicpc.net/problem/9658

n = int(input())
dp = [0] * 1001
dp[1], dp[2], dp[3], dp[4] = 'CY', 'SK', 'CY' , 'SK'

for i in range(5, n+1) :
    if 'CY' in [dp[i-1], dp[i-3], dp[i-4]] :
        dp[i] = 'SK'
    else : 
        dp[i] = 'CY'

print(dp[n])