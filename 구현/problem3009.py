# https://www.acmicpc.net/problem/3009
x = []
y = []

for _ in range(3) :
    _x, _y = map(int,input().split())
    x.append(_x)
    y.append(_y)

for _x in x :
    if x.count(_x) == 1 :
        print(_x, end = ' ') 

for _y in y :
    if y.count(_y) == 1 :
        print(_y, end = ' ')         