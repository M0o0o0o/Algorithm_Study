n,m = map(int, input().split())

INF = int(1e9)
graph = [[0]* (n+1) for _ in range (n+1)]

rank = [[0]*2 for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == 1 :
            rank[i][1] += (1 + rank[j][1])
            rank[j][0] += (1 + rank[i][0])

result = 0
for i in range(1, n+1) :
    if sum(rank[i]) >= (n-1) :
        result += 1

print(result)