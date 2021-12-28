# https://www.acmicpc.net/problem/5676


import sys
input = sys.stdin.readline

def init(start, end, index) :
    if start == end : 
        tree[index] = lst[start]
        return tree[index]
    mid = (start + end) // 2 
    tree[index] = init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)
    return tree[index]

def interval(start, end, index, left, right):
    if right < start or end < left:
        return 1
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval(start, mid, index * 2, left, right) * interval(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, what, value):
    if start == end : 
        tree[index] = value
        return
    mid = (start + end ) // 2
    if what <= mid : update(start, mid, index * 2, what ,value)
    else : update(mid + 1, end, index * 2 + 1, what, value)
    tree[index] = tree[index * 2] * tree[index * 2 + 1]

while True :
    try : 
        n, m = map(int ,input().split())
        lst = list(map(int, input().split()))
        tree = [0] * (len(lst) * 4)
        init(0, n-1, 1)
        ans = '';
        for _ in range(m):
            mod, a, b = input().split()
            if mod == 'P':
                value = interval(0, len(lst)-1, 1, int(a)-1, int(b)-1)
                if value == 0 : ans += '0'
                elif value > 0 : ans += '+'
                else : ans += '-'
            else:
                update(0, len(lst)-1, 1, int(a)-1, int(b))
        print(ans)
    except Exception: break
    
