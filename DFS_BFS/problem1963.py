# https://www.acmicpc.net/problem/1963
import math
from collections import deque

n = 10000
array = [True for i in range(n)] 
array[1] = 0 
prime = []

for i in range(2, int(math.sqrt(n)) + 1): 
    if array[i] == True: 
        j = 2 
        while i * j < n:
            array[i * j] = False
            j += 1

for i in range(1000, 10000) :
    if array[i] :
        prime.append(i)


def check(a, b) :
    a, b = str(a), str(b)
    count = 0
    for i in range(4) :
        if a[i] != b[i] :
            count += 1
    if count == 1 :
        return True
    return False

for _ in range(int(input())) :
    start, target = map(int,input().split())
    visited = [-1] * (10000)
    q = deque([start])
    visited[start] = 0

    while q : 
        num = q.popleft()
        if num == target : 
            break

        for p in prime : 
            if check(num, p) and visited[p] == -1 : 
                q.append(p) 
                visited[p] = visited[num] + 1

    if visited[target] == -1 :
        print('Impossible')
    else :
        print(visited[target])

