# https://programmers.co.kr/learn/courses/30/lessons/12952

def dfs(q, n, r):
    cnt = 0
    if r == n:
        return 1
    for c in range(n):
        q[r] = c
        for x in range(r):
            if q[x] == q[r]:
                break
            if abs(q[x]-q[r]) == (r-x):
                break
        else:
            cnt += dfs(q, n, r+1)
    return cnt


def solution(n):
    q = [0] * n
    return dfs(q, n, 0)


print(solution(4))
