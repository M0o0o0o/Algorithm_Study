# https://programmers.co.kr/learn/courses/30/lessons/42898


def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if (i,j) == (1,1) : continue
            if [j,i] in puddles :
                dp[i][j] = 0 
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m]  % 1000000007
print(solution(4,3,[[2, 2]]))