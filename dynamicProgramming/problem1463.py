# https://www.acmicpc.net/problem/1463

n = int(input())
dp = [0] * (n+1)
store = [[] for _ in range(n+1)]

for i in range(2, n+1) :
    dp[i] = dp[i-1] + 1
    store[i] += store[i-1] + [i]
    if i % 3 == 0 :
        if dp[i] > dp[i // 3] + 1: 
            store[i] = store[i//3] + [i]
            dp[i] = dp[i//3] + 1

    if i % 2 == 0 :
        if dp[i] > dp[i // 2] + 1: 
            store[i] = store[i//2] + [i]
            dp[i] = dp[i//2] + 1
print(dp[n])
print(*store[n][::-1], 1)