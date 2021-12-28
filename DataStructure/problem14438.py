# https://www.acmicpc.net/problem/14438

import sys
input = sys.stdin.readline

def init(start, end, index) :
    if start == end : 
        tree[index] = lst[start]
        return tree[index]
    mid = (start + end) // 2 
    tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]

def interval(start, end, index, left, right):
    if right < start or end < left:
        return int(1e9)
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return min(interval(start, mid, index * 2, left, right), interval(mid + 1, end, index * 2 + 1, left, right))


def update(start, end, index, what, value):
    if start == end : 
        tree[index] = value
        return
    mid = (start + end ) // 2
    if what <= mid : update(start, mid, index * 2, what ,value)
    else : update(mid + 1, end, index * 2 + 1, what, value)
    tree[index] = min(tree[index * 2], tree[index * 2 + 1])


n = int(input())

lst = list(map(int, input().split()))
tree = [0] * (len(lst) * 4)
m = int(input())
init(0, n-1, 1)

for _ in range(m):
    mod, a, b = map(int, input().split())
    if mod == 2:
        print(interval(0, len(lst)-1, 1, a-1, b-1))
    else:
        update(0, len(lst)-1, 1, a-1, b)
