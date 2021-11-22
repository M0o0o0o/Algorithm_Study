# https://www.acmicpc.net/problem/10103

import sys 
input = sys.stdin.readline

n = int(input())
A,B = 100,100 

for _ in range(n) :
    a,b = map(int, input().split())
    if a > b :
        B -= a 
    if a < b :
        A -= b
        
print(A)
print(B)

