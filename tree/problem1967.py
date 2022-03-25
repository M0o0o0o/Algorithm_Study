# https://www.acmicpc.net/problem/1967

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 트리를 돌면서 왼쪽 오른쪽 자식이 있다면 돌면서
# distance[i][0], distance[i][1]을 업데이트 한다.


def dfs(node):
    if node not in tree:
        return cost[node]
    # 이제 각 자식 노드들을 반복문 돈다.
    lst = [0]
    for nextNode in tree[node]:
        lst.append(dfs(nextNode))
    lst.sort(reverse=True)
    # 해당 노드의 값 정리
    distance[node] += lst[0] + lst[1]
    return lst[0] + cost[node]


tree = dict()
n = int(input())
distance = [0 for _ in range(n+1)]
cost = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    cost[b] = c
    if a not in tree:
        tree[a] = [b]
        continue
    tree[a].append(b)

dfs(1)
print(max(distance))
# 결국 한 노드를 기점으로 자식들을 연결해서 가장 큰 지름이 되는 것을 업데이트 하면 된다.
# 각 노드에 대한 distance 배열을 두고
# 왼쪽 자식과 오른쪽 자식에 대한 값을 업데이트 한다.
