# https://www.acmicpc.net/problem/2167

n, m = map(int,input().split())
graph = []

for _ in range(n) :
    graph.append(list(map(int,input().split())))

tc = int(input())

for _ in range(tc) :
    i, j, x, y = map(int,input().split())
    i, j, x, y = i - 1, j -1, x -1, y - 1
    answer = 0 
    for a in range(i, x+1) :
        for b in range(j, y+1) :
            answer += graph[a][b]
    print(answer)