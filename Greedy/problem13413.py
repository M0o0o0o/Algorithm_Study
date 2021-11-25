# https://www.acmicpc.net/problem/13413

import sys; input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    a, t = list(input().strip('\n')), list(input().strip('\n'))
    black, white = 0, 0
    
    for i in range(n) :
        if a[i] != t[i] : 
            if a[i] == 'B' : black += 1
            else : white += 1
    
    print(max(black, white))
                
