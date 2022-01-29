#https://www.acmicpc.net/problem/2011

word = list(map(int, input()))
length = len(word)

dp = [0] * (length + 1)

if word[0] == 0 :
    print(0)
else :
    word = [0] + word
    dp[0], dp[1] = 1, 1
    
    for i in range(2, length + 1) : 
        one = word[i]
        two =  word[i-1] * 10 + word[i]
        if 1 <= one <= 9 : 
            dp[i] += dp[i-1] 
        if 10 <= two <= 26 : 
            dp[i] += dp[i-2]
        dp[i] %= 1000000
        
    print(dp[length])