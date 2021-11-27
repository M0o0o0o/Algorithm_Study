# https://www.acmicpc.net/problem/2720

import sys
input = sys.stdin.readline
for _ in range(int(input())) :
    n = int(input())
    for m in [25,10,5,1] : 
        print(n // m, end = ' ')
        n %= m 
    print()        