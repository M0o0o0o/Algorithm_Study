# https://www.acmicpc.net/problem/13419

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    word = input().strip('\n')

    a, b = word[0], ""
    i, cnt = 0, 0
    while True:
        i = i + 1 if i + 1 < len(word) else 0
        cnt += 1
        if cnt % 2 == 0:
            if word[i] == a[0]:
                break
            a += word[i]
            continue
        else:
            b += word[i]

    print(a)
    print(b)
# b 차례


# 4
# ABC
# ABCFXZ
# K
# DY
