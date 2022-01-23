# https://www.acmicpc.net/problem/10174


for _ in range(int(input())):
    s = input().lower()
    if s == s[::-1]:
        print('Yes')
    else:
        print('No')
