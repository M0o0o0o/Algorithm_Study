# https://www.acmicpc.net/problem/2493

import heapq

n = int(input())
lst = [0] + list(map(int,input().split()))
answer = [0]
stack = [(lst[1], 1)]
for i in range(2, n+1) :
    receive = 0
    while stack : 
        if lst[i] > stack[-1][0] : 
            stack.pop()
        else :
            receive = stack[-1][1]
            break
    stack.append((lst[i], i))
    answer.append(receive)

for i in answer : 
    print(i, end = ' ')