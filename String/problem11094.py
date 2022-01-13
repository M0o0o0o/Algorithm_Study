# https://www.acmicpc.net/problem/11094

for _ in range(int(input())):
    s = input()
    if s.count('Simon says') == 1:
        print(s[10:])
