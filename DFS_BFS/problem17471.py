# https://www.acmicpc.net/problem/17471

from itertools import combinations
from collections import deque

def make_two(one) :
    two = []
    for i in combi_lst :
        if i not in one : 
            two.append(i)
    return two

def bfs(target) :
    visited = [False] * (n+1)
    q = deque()
    q.append(target[0])
    visited[target[0]] = True

    while q : 
        x = q.popleft()
        for nx in graph[x] :
            if nx in target and not visited[nx] :
                visited[nx] = True
                q.append((nx))

    total = 0 

    for node in target :
        if not visited[node] :
            return int(1e9) 
        total += value[node] 

    return total


n = int(input())
graph =[[] for _ in range(n+1)]
combi_lst = [i for i in range(1, n+1)]
value = [0] + list(map(int,input().split()))
answer= int(1e9) 


for a in range(1,n + 1) :
    lst = list(map(int,input().split()))
    del lst[0]
    for b in lst :
        graph[a].append(b)
        
for c in range(1, (n // 2) + 1) :

    lst = [1]
    lst = list(combinations(combi_lst, c))
    for l in lst :

        one = list(l)
        two = make_two(one)
        ototal = bfs(one)
        ttotal = bfs(two) 

        if int(1e9) in [ototal, ttotal] : continue

        answer = min(answer, abs(ototal-ttotal))

if answer < int(1e9) :
    print(answer)
else :
    print(-1)