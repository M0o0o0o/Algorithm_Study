# https://www.acmicpc.net/problem/11586

n = int(input())
mirror = []
for _ in range(n) :
    mirror.append(list(input()))
mode = int(input())

if mode == 1: 
    for i in range(n) :
        for j in range(n) :
            print(mirror[i][j], end = '')
        print()
elif mode == 2:
    for i in range(n) :
        for j in range(n-1, -1, -1) : 
            print(mirror[i][j], end = '')
        print()
else :
    for i in range(n-1, -1, -1) :
        for j in range(n) :
            print(mirror[i][j], end = '')
        print()        
        
        