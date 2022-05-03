# https://www.acmicpc.net/problem/14696

def Input():
    lst = list(map(int, input().split()))
    return [lst[1:].count(4), lst[1:].count(3), lst[1:].count(2), lst[1:].count(1)]


for _ in range(int(input())):
    aLst, bLst = Input(), Input()
    if aLst[0] != bLst[0]:
        print('A' if aLst[0] > bLst[0] else 'B')
    elif aLst[1] != bLst[1]:
        print('A' if aLst[1] > bLst[1] else 'B')
    elif aLst[2] != bLst[2]:
        print('A' if aLst[2] > bLst[2] else 'B')
    elif aLst[3] != bLst[3]:
        print('A' if aLst[3] > bLst[3] else 'B')
    else:
        print('D')
