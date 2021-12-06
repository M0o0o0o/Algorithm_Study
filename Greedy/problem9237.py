# https://www.acmicpc.net/problem/9237

import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 1
for i in range(n) :
    lst[i] -= i
print(max(lst) + 1 + n)

