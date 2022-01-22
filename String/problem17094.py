# https://www.acmicpc.net/problem/17094

n = int(input())
s = input()
two, e = s.count('2'), s.count('e')
if two > e : print('2')
elif two < e : print('e')
else : print('yee')