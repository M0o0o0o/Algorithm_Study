# https://www.acmicpc.net/problem/5557

n = int(input())
lst = list(map(int,input().split()))
dp = [[0] * 21 for _ in range(n)]
dp[0][lst[0]] = 1

for i in range(1,n-1) :
    for j in range(21) :
        if dp[i-1][j] != 0 :
            add, sub = j + lst[i], j - lst[i]
            if 0 <= add <= 20 : dp[i][add] += dp[i-1][j]
            if 0 <= sub <= 20 : dp[i][sub] += dp[i-1][j]
        
print(dp[n-2][lst[n-1]])
# for i in range(n) :
#     print(dp[i])