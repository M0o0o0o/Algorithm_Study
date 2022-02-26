# https://www.acmicpc.net/problem/9492

while True:
    n = int(input())
    if n == 0:
        break
    lst = [input().strip('\n') for _ in range(n)]
    R = n // 2 if n % 2 == 0 else (n//2) + 1
    r = R
    for l in range(0, R):
        print(lst[l])
        if r < n:
            print(lst[r])
            r += 1
