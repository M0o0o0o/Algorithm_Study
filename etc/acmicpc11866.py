# https://www.acmicpc.net/problem/11866

from collections import deque
n, k = map(int,input().split())
lst = deque([i for i in range(1,n+1)])
result = []

while len(lst) > 0 :
    index = 1
    while True: 
        buf = lst.popleft()
        if index == k :
            result.append(buf)
            break
        else :
            lst.append(buf)
        index += 1


print('<', end = '')
for i in range(n) :
    if i != n-1 :
        print(result[i], end=', ')
    else :
        print(result[i], end='')

    
print('>', end = '')
