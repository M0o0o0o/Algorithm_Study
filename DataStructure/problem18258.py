# https://www.acmicpc.net/problem/18258

from collections import deque
import sys
n = int(input())
q = deque()

def empty() :
    if q : return False
    print('-1')
    return True



for com in range(n) :
    com = list(map(str, sys.stdin.readline().split()))

    if com[0] == 'push' : q.append(com[1])
    if com[0] == 'pop' and not empty() : print(q.popleft())
    if com[0] == 'size' : print(len(q))
    if com[0] == 'empty' :
        if q : print(0)
        else : print(1) 
    if com[0] == 'back' and not empty() : print(q[-1])
    if com[0] == 'front' and not empty() : print(q[0])

