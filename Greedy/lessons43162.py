# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

visit = [False] * 2222
def solution(n, computers):
    global visit
    answer = 0

    for i in range(n):
        if not visit[i] :
            answer += 1
            bfs(i,computers,n)
    return answer

def bfs(com, computers, n) :
    global visit
    q = deque([com])
    visit[com] = True
    while q :
        c = q.popleft()
        for i in range(n) :
            if i == c :
                continue
            if visit[i] == False and computers[c][i] == 1 :
                q.append(i)
                visit[i] = True
    return 


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
