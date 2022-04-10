# https://programmers.co.kr/learn/courses/30/lessons/12929


def dfs(rLeft, rRight, left):
    global ans
    cnt = 0
    if rLeft == 0 and rRight == 0:
        return 1
    if rLeft > 0:
        cnt += dfs(rLeft-1, rRight, left + 1)
    if rRight > 0 and left > 0:
        cnt += dfs(rLeft, rRight - 1, left - 1)
    return cnt


def solution(n):
    return dfs(n, n, 0)


print(solution(2))
print(solution(3))
