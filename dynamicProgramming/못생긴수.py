n = int(input())

dp = [0] * n
dp[0] = 1

twoIndex = threeIndex = fiveIndex = 0
two = 2
three = 3
five = 5

for i in range(1, n) :
    dp[i] = min(two, three, five)

    if dp[i] == two :
        twoIndex += 1
        two = dp[twoIndex] * 2
    if dp[i] == three :
        threeIndex += 1
        three = dp[threeIndex] * 3
    if dp[i] == five :
        fiveIndex += 1
        five = dp[fiveIndex] * 5

print(dp[n-1])