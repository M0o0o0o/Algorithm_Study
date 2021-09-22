# https://www.acmicpc.net/problem/10996
n = int(input())
a = '*' 
b = ' '
for i in range(n) :
    if a[len(a) -1 ] == '*' :
        a += ' '
        b += '*'
    else :
        a += '*'
        b += ' '

if a[n-1] == ' ' : a = a[0:n]
if b[n-1] == ' ' : b = b[0:n]

for _ in range(n) :
    print(a + "\n" + b)
