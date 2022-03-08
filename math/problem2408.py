# https://www.acmicpc.net/problem/2408

eq = ''
n = int(input())
for _ in range(n + n - 1):
    eq += input()
eq = eq.replace('/', '//')
print(eval(eq))
