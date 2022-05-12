# https: // www.acmicpc.net/problem/2668

from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node, visited):
    visited.add(node)
    checked[node] = 1
    for nn in graph[node]:
        if nn not in visited:
            dfs(nn, visited.copy())
        else:
            ans.extend(list(visited))
            return


n = int(input())
graph = defaultdict(list)
for i in range(1, n+1):
    v = int(input())
    graph[v].append(i)

checked = [0 for _ in range(n+1)]
ans = []
for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set([]))

ans.sort()
print(len(ans))
for a in ans:
    print(a)
