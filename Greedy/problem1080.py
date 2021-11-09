# https://www.acmicpc.net/problem/1080

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph, target = [], []

def convert(i,j) :
    for x in range(i, i+3):
        for y in range(j, j+3) :
            graph[x][y] = 1 - graph[x][y]

for i in range(n) :
    graph.append(list(map(int, input().strip('\n'))))
for i in range(n) :
    target.append(list(map(int, input().strip('\n'))))
        
ans = 0
for i in range(n-2) :
    for j in range(m-2) :
        if graph[i][j] != target[i][j] :
            convert(i,j)
            ans += 1
            
for i in range(n) :
    for j in range(m) :
        if graph[i][j] != target[i][j] :
            print(-1) 
            exit(0)

print(ans)