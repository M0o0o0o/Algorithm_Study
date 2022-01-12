# https://www.acmicpc.net/problem/13420

for _ in range(int(input())):
    left, right = input().split('=')
    if eval(left) == int(right) :
        print('correct')
    else :
        print('wrong answer')
