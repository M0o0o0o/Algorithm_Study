# https://www.acmicpc.net/problem/1225

A, B = input().split()
ans = 0
for a in list(map(int, A)):
    if a == 0:
        continue
    for b in list(map(int, B)):
        if b == 0:
            continue
        ans += (a * b)

print(ans)
