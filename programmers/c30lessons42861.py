# https://programmers.co.kr/learn/courses/30/lessons/42861


def find_parent(parents, node):
    if node != parents[node]:
        parents[node] = find_parent(parents, parents[node])
    return parents[node]


def union_parent(parents, a, b):
    a, b = find_parent(parents, a), find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def solution(n, costs):
    ans = 0
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    for cost in costs:
        a, b, c = cost
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            ans += c

    return ans


print(solution(4,	[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
