# https://programmers.co.kr/learn/courses/30/lessons/12914


def solution(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]


print(solution(1))
print(solution(4))
print(solution(3))
