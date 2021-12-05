# https://www.acmicpc.net/problem/14241

import sys; input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for i in range(1,n) :
    ans += lst[i] * lst[i-1]
    lst[i] += lst[i-1]
print(ans)
    