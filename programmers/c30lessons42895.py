# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    ans = -1
    dp = [[] for _ in range(9)]
    for i in range(1, 9):
        dp[i].append(int(str(N) * i))
        for j in range(1, i):
            for first in dp[j]:
                for second in dp[i-j]:
                    dp[i].append(first + second)
                    dp[i].append(first-second)
                    dp[i].append(first * second)
                    if second:
                        dp[i].append(first // second)
        dp[i] = list(set(dp[i]))
        if number in dp[i]:
            ans = i
            break
    return ans


print(solution(5, 12))
