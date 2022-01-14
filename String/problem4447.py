# https://www.acmicpc.net/problem/4447

for _ in range(int(input())):
    s = input()
    b, g = s.count('b') + s.count('B'),  s.count('g') + s.count('G')
    if b > g:
        print(s + ' is A BADDY')
    elif b < g:
        print(s + ' is GOOD')
    else:
        print(s + ' is NEUTRAL')
