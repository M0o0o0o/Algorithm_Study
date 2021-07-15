# https://www.acmicpc.net/problem/9251

a = input()
b = input()

aLen = len(a)
bLen = len(b) 

dp = [[0] * (bLen+1) for _ in range(aLen+1) ]
result = 0

for i in range(1, aLen+1) :
    for j in range(1, bLen +1 ) :
        if a[i-1] == b[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        result = max(result, dp[i][j])


print(result)