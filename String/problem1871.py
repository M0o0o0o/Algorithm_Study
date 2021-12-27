# https://www.acmicpc.net/problem/1871

for _ in range(int(input())):
    a,b = list(input().split('-'))
    b = int(b)
    result = 0
    for i in range(len(a)) :
        result += (ord(a[i]) - 65) * (26 ** (len(a) - 1 - i)) 
    if abs(result - b ) <= 100 : print('nice')
    else : print('not nice')