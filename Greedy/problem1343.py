# https://www.acmicpc.net/problem/1343

import sys
input = sys.stdin.readline

def changeA(s,e) :
    for i in range(s,e+1) :
        lst[i] = 'A'
def changeB(s,e) :
    for i in range(s,e+1) :
        lst[i] = 'B'
        
lst = list(input().strip('\n')) + ['.']
s, e = 0, 0

for i in range(1,len(lst)) :
    if lst[i-1] == '.' : 
        s, e = i, i
    if lst[i] == 'X' :
        e = i 
        if e - s == 3 :
            changeA(s,e) 
            s = e + 1
        elif e - s == 1 and lst[i+1] == '.' : 
            changeB(s,e)
            s = e + 1

if lst.count('X') > 0 : 
    print(-1)
else :
    print(''.join(lst[:len(lst)-1]))

            

    