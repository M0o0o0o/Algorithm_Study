# https://www.acmicpc.net/problem/16172
A, b = list(input()), list(input())
a = ['' if 48 <= ord(A[i]) <= 57 else A[i] for i in range(len(A))]

if ''.join(a).find(''.join(b)) != -1 : print(1)
else : print(0)
