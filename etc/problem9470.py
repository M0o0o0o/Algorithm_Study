# https://www.acmicpc.net/problem/9470

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m+1)]
    indegree = [0] * (m+1)
    order = [0] * (m+1)
    q = deque([])
    cnt = [[0, 0]] * (m+1)

    for i in range(p):
        a, b, = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    for i in range(1, m+1):
        if indegree[i] == 0:
            cnt[i] = [1, 1]
            q.append(i)

    while q:
        now = q.popleft()
        if cnt[now][1] >= 2:
            order[now] = cnt[now][0] + 1
        else:
            order[now] = cnt[now][0]

        for node in graph[now]:
            indegree[node] -= 1
            if cnt[node][0] == order[now]:
                cnt[node][1] += 1
            elif cnt[node][0] < order[now]:
                cnt[node] = [order[now], 1]
            if indegree[node] == 0:
                q.append(node)

    print(k, order[m])
