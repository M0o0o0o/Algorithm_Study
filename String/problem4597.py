# https://www.acmicpc.net/problem/4597

import sys
input = sys.stdin.readline

while True:
    bits = list(input().strip('\n'))
    if bits[0] == '#':
        break
    one = 2
    for b in bits[:len(bits)-1]:
        if b == '1':
            one += 1
    if (bits[-1] == 'e' and one % 2 == 0) or (bits[-1] == 'o' and one % 2 == 1):
        print(''.join(bits[:len(bits)-1]) + '0')
    else:
        print(''.join(bits[:len(bits)-1]) + '1')
