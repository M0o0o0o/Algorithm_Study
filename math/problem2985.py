# https://www.acmicpc.net/problem/2985

a, b, c = map(int, input().split())
lst = [('+', '=='), ('-', '=='), ('*', '=='), ('/', '=='), ('==', '+'), ('==', '-'), ('==', '/'), ('==', '*')
       ]

for i in range(8):
    string = str(a) + lst[i][0] + str(b) + lst[i][1] + str(c)
    if eval(string):
        print(string.replace('==', '='))
        break
