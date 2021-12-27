# https://www.acmicpc.net/problem/2042
import sys 
input = sys.stdin.readline

def init(start, end ,index) :
    if start == end : 
        tree[index] = lst[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def interval(start, end, index, left, right) :
    if right < start or end < left : return 0
    if left <= start and right >= end : 
        return tree[index]
    mid = (start + end) // 2
    return interval(start, mid, index * 2, left, right) + interval(mid + 1, end, index * 2 + 1, left, right)

def update(start, end, index, what, value):
    if start == end : 
        tree[index] = value
        return
    mid = (start + end ) // 2
    if what <= mid : update(start, mid, index * 2, what ,value)
    else : update(mid + 1, end, index * 2 + 1, what, value)
    tree[index] = tree[index * 2] + tree[index * 2 + 1]

n, m, k = map(int, input().split())
lst, tree = [], [0] * (n * 4)
for _ in range(n) :
    lst.append(int(input()))

init(0, len(lst)-1, 1)

for _ in range(m + k) :
    a, b, c = map(int, input().split())
    if a == 1 : 
        update(0, len(lst)-1, 1, b-1, c)
    else :
        print(interval(0, len(lst)-1, 1, b-1, c-1))
        
    
    