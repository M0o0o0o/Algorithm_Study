# https://www.acmicpc.net/problem/11048

n, m = map(int, input().split())
graph = []

for _ in range(n) :
    graph.append(list(map(int,input().split())))

for i in range(n) :
    for j in range(m) :
        left = graph[i-1][j] if i-1 >= 0 else 0
        right = graph[i][j-1] if j-1 >= 0 else 0
        back = graph[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
        graph[i][j] += max(left, right, back)

print(graph[n-1][m-1])
