# https://www.acmicpc.net/problem/2407

import sys
sys.setrecursionlimit(10**5)
n, m = map(int,input().split())


def recur(num) :
    if num == 1 : return 1
    return num * recur(num - 1)

print(recur(n) // (recur(n-m) * recur(m)))