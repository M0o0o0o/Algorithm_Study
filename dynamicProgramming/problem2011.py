# https://www.wordcmicpc.net/problem/2011

a = list(map(int, list(input())))
l = len(a)
dp = [0] * (l+1)

if a[0] == 0: 
    print(0)
else :
    a = [0] + a 
    dp[0] = 1
    dp[1] = 1 

    for i in range(2, l+1):
        cur = a[i] 
        cur2 = a[i-1] * 10 + a[i] 
        if cur >= 1 and cur <= 9:
            dp[i] += dp[i-1]
        if cur2 >= 10 and cur2 <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000
    print(dp[l])