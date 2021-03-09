#https://www.acmicpc.net/problem/18352

# n : 도시의 개수, m : 도로의 개수, k : 거리 정보 x : 출발 도시  

#bfs를 돌며 


from collections import deque
n, m, k, x   = map(int, input().split())


graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0

for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)


queue = deque([x])
while queue :
    v = queue.popleft()
    for i in graph[v] :
        if distance[i] == -1 :
            distance[i] = distance[v] + 1
            queue.append(i)

answer = False

for i in range(1, n+1) :
    if distance[i] == k :
        print(i)
        answer = True

if answer == False :
    print(-1)   