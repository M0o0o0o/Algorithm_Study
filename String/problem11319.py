# https://www.acmicpc.net/problem/11319

vowels = ['a', 'e', 'i', 'o', 'u']
for _ in range(int(input())):
    c, v = 0, 0
    for s in input().replace(' ', ''):
        if s.lower() in vowels:
            v += 1
        else:
            c += 1
    print(c, v)
