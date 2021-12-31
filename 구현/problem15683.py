# https://www.acmicpc.net/problem/15683
import copy

def watch(graph, x, y, D) : 
    for d in D : 
        nx, ny = x + dx[d], y + dy[d] 
        while True : 
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '6' : 
                graph[nx][ny] = '#'
                nx, ny = nx + dx[d], ny + dy[d]
            else : break


def dfs(index, graph, progress) :
    global ans 
    if index == len(cctv) : 
        count = 0 
        for i in range(n) :count += graph[i].count('0')
        ans = min(ans, count)
        return
    graph2 = copy.deepcopy(graph)
    for D in direction[cctv[index][2]] :
        watch(graph2, cctv[index][0], cctv[index][1], D)
        dfs(index + 1, graph2, progress+ [D])
        graph2 = copy.deepcopy(graph)
    

n, m = map(int, input().split())
graph = []
cctv = []
ans = int(1e9)
dx, dy = [0,1,0,-1], [1,0,-1,0]
direction = [0, [[0],[1],[2],[3]], [[0,2], [1,3]], [[0,3],[0,1],[1,2],[2,3]], [[0,2,3],[3,0,1],[0,1,2],[1,2,3]], [[0,1,2,3]]]

for i in range(n) :
    graph.append(list(input().split(' ')))
    for j in range(m) :
        if '1' <= graph[i][j] <= '5' :
            cctv.append((i, j, int(graph[i][j])))
            

dfs(0, graph, [])
print(ans)
