from collections import deque

for _ in range(int(input())):
    n = int(input())
    indgree = [0] * (n+1)

    graph = [[0] * (n+1) for i in range(n+1)]
    lst = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            indgree[lst[j]] += 1
            graph[lst[i]][lst[j]] = 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b] == 0:
            graph[a][b] = 1
            graph[b][a] = 0
            indgree[a] -= 1
            indgree[b] += 1
        else:
            graph[a][b] = 0
            graph[b][a] = 1
            indgree[a] += 1
            indgree[b] -= 1

    result = []
    q = deque()

    for i in range(1, n+1):
        if indgree[i] == 0:
            q.append(i)

    only = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            only = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j] == 1:
                indgree[j] -= 1
                if indgree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not only:
        print('?')
    else:
        for i in result:
            6
            print(i, end=' ')
        print()