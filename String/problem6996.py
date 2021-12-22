# https://www.acmicpc.net/problem/6996

for _ in range(int(input())):
    a, b = input().split()
    if len(a) != len(b):
        print(a, '&', b, 'are NOT anagrams.')
        continue
    check = True
    for s in b:
        if b.count(s) > a.count(s):
            check = False
            break
    if check:
        print(a, '&', b, 'are anagrams.')
    else:
        print(a, '&', b, 'are NOT anagrams.')
