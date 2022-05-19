# https://www.acmicpc.net/problem/21276

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ans, graph, indegree = dict(), dict(), dict()

for l in list(input().strip('\n').split(' ')):
    ans[l] = []
    graph[l] = []
    indegree[l] = 0

for _ in range(int(input())):
    a, b = input().strip('\n').split()
    graph[b].append(a)
    indegree[a] += 1

q = []
for key in indegree.keys():
    if indegree[key] == 0:
        q.append(key)

print(len(q))
print(*sorted(q))
q = deque(q)
while q:
    now = q.popleft()
    for node in graph[now]:
        indegree[node] -= 1
        if indegree[node] == 0:
            ans[now].append(node)
            q.append(node)

for key in sorted(ans.keys()):
    if not ans[key]:
        print(key, 0)
        continue
    print(key, len(ans[key]), *sorted(ans[key]))
