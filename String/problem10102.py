# https://www.acmicpc.net/problem/10102

n = int(input())
ab = list(input().strip('\n'))
a = ab.count('A')
b = ab.count('B')

if a > b : print('A')
elif a < b : print('B')
else : print('Tie')
