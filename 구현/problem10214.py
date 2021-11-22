# https://www.acmicpc.net/problem/10214
import sys; input = sys.stdin.readline

for _ in range(int(input())) :
    A,B = 0,0
    for _ in range(9) :
        a,b = map(int, input().split())
        A += a
        B += b
    if A > B : print('Yonsei')
    elif A < B : print('Korea')
    else : print('Draw')
    
    