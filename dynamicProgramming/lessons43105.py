# https://programmers.co.kr/learn/courses/30/lessons43105

def dfs(triangle, dp, i, j) :
    if i == len(triangle) -1  :
        return triangle[i][j]
    if dp[i][j] != 0 : return dp[i][j]
    
    dp[i][j] += triangle[i][j] + max(dfs(triangle, dp, i+1, j), dfs(triangle, dp, i+1, j+1))
    
    return dp[i][j]

def solution(triangle):
    dp = [] * len(triangle)
    for i in range(len(triangle)) :
        dp.append([0] * len(triangle[i]))
    return dfs(triangle, dp, 0, 0)

# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))