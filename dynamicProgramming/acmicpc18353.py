# https://www.acmicpc.net/problem/18353

n = int(input())
lst = list(map(int,input().split()))
dp = [1] * n;


for i in range(n) :
    for j in range(0, i) :
        if lst[j] > lst[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
