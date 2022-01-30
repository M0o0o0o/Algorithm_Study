# https://www.acmicpc.net/problem/23027

s = input()
n = len(s)
tmpA = 'BCDF'
tmpB = 'CDF'
tmpC = 'DF'

if 'A' in s:
    for i in s:
        if i in tmpA:
            s = s.replace(i, 'A')
elif 'B' in s:
    for i in s:
        if i in tmpB:
            s = s.replace(i, 'B')
elif 'C' in s:
    for i in s:
        if i in tmpC:
            s = s.replace(i, 'C')
else:
    s = 'A'*n
print(s)
