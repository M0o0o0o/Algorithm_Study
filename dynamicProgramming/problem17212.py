# https://www.acmicpc.net/problem/17212

m = int(input())
dp = [int(1e9)] * 100001
dp[0], dp[1], dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] = 0, 1, 1, 2, 2, 1, 2, 1

for i in range(8, m+1) :
    for j in [1,2,5,7] :
        dp[i] = min(dp[i], dp[i-j] + 1)
        
print(dp[m])
