# https://www.acmicpc.net/problem/9252

a = [0] + list(input())
b = [0] + list(input())
n, m = len(a), len(b)

dp = [[0] * m for _ in range(n+1)]

for i in range(1,n) :
    for j in range(1,m) :
        if a[i] == b[j] :
            dp[i][j] = dp[i-1][j-1] + 1 
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = n-1, m-1

print(dp[i][j])
result = ""
while i > 0 and j > 0 :
    if dp[i][j] == dp[i-1][j] :
        i -= 1
    elif dp[i][j] == dp[i][j-1] :
        j -= 1
    else :
        result += a[i]
        i -= 1
        j -= 1
print(result[::-1])
