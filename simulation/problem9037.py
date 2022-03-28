# https://www.acmicpc.net/problem/9037

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst = [l + 1 if l % 2 != 0 else l for l in lst]
    cnt = 0
    fromTo = [0 for _ in range(n+1)]

    while lst.count(lst[0]) != n:
        for i in range(n):
            fromTo[i+1] = lst[i] // 2
            lst[i] -= lst[i] // 2
        fromTo[0] = fromTo[n]

        for i in range(n):
            lst[i] += fromTo[i]
        lst = [l + 1 if l % 2 != 0 else l for l in lst]
        cnt += 1
    print(cnt)
