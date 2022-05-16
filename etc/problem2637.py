# https://www.acmicpc.net/problem/2637

from collections import deque
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())

indgree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
basic = set()
ans = [dict() for _ in range(n+1)]

for _ in range(m):
    # x를 만드는데 y가 cost만큼 든다
    x, y, cost = map(int, input().split())
    graph[y].append((x, cost))
    indgree[x] += 1

q = deque([])

for i in range(1, n+1):
    if indgree[i] == 0:
        q.append(i)
        basic.add(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        node, cost = i
        if now in basic:
            # 기본 일 때와 아닐 때를 비교해서 처리해야 한다.
            if now not in ans[node]:
                ans[node][now] = cost
            else:
                ans[node][now] += cost
        else:
            # 중간 부품일 경우
            for key in ans[now]:
                if key not in ans[node]:
                    ans[node][key] = ans[now][key] * cost
                else:
                    ans[node][key] += ans[now][key] * cost

        indgree[node] -= 1
        if indgree[node] == 0:
            q.append(node)

ans = [(key, ans[n][key]) for key in ans[n]]
ans.sort()

for a in ans:
    print(a[0], a[1])
