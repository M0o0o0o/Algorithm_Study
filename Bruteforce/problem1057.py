# https://www.acmicpc.net/problem/1057

n, a, b = map(int,input().split())

_round = 1

while True :
    if (a//2) + (a%2) == (b//2) + (b%2) :
        print(_round)
        break

    a = (a//2) + (a%2)
    b = (b//2) + (b%2)
    
    _round += 1

