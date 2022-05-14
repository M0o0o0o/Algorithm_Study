def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * n

for i in range(n):
    parent[i] = i

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(parent, i, j)

result = 'YES'
root = find_parent(parent, plan[0])

for i in range(1, len(plan)):
    if root != find_parent(parent, plan[i]):
        result = 'NO'
        break

print(result)
