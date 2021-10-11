# https://www.acmicpc.net/problem/2251

from collections import deque

def check(x,y) :
    if not visited[x][y] :
        visited[x][y] = True
        q.append((x,y))

def bfs() :
    while q : 
        a, b = q.popleft()
        c = z - (a+b)

        if a == 0 :
            answer.append(c)
        # a -> b
        value = min(a, y-b)
        check(a - value, b + value)
        #a > c 
        value = min(a, z-c) 
        check(a-value, b)
        #b->a
        value = min(b, x-a)
        check(a+value, b-value)
        #b->c
        value = min(b, z-c)
        check(a, b-value)
        #c->a
        value = min(c, x-a)
        check(a+value, b)
        #c->b
        value = min(c, y-b)
        check(a, b+value)



x,y,z = map(int,input().split())

answer = []
visited = [[False] * (y+1) for _ in range(x+1)] 
visited[0][0] = True
q = deque([(0,0)])

bfs()
answer.sort()

for i in answer :
    print(i, end = ' ')