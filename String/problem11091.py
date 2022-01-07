# https://www.acmicpc.net/problem/11091

for _ in range(int(input())):
    alpha = [0] * 26
    for a in list(input()) : 
        if a.isalpha() : 
            alpha[ord(a.upper()) - 65] += 1
    if alpha.count(0) > 0: 
        print('missing', ''.join([chr(i + 65).lower() for i in range(26) if alpha[i] == 0 ]), end = '\n')
    else :
        print('pangram')