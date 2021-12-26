# https://www.acmicpc.net/problem/2268

import sys
input = sys.stdin.readline


def interval_sum(start, end, index, left, right):
    if right < start or end < left:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


n, m = map(int, input().split())

lst = [0] * n
tree = [0] * (len(lst) * 4)

for _ in range(m):
    mod, a, b = map(int, input().split())
    if mod == 0:
        print(interval_sum(0, len(lst)-1, 1,
                           min(a-1, b-1), max(a-1, b-1)))
    else:
        update(0, len(lst)-1, 1, a-1, b)
