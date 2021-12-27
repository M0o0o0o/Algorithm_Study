# https://www.acmicpc.net/problem/11328

for _ in range(int(input())) :
    a,b = map(list, input().split())
    a.sort()
    b.sort()
    if ''.join(a) == ''.join(b) : print('Possible')
    else : print('Impossible')