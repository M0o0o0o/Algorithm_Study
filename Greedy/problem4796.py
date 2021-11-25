# https://www.acmicpc.net/problem/4796
import sys; input = sys.stdin.readline
i = 1
while True : 
    l,p,v = map(int ,input().split())
    if l + p + v == 0 : break
    print("Case " + str(i) + ":", l * (v // p) + (min(v % p, l))) 
    i += 1