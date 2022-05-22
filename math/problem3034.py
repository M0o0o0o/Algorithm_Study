# https://www.acmicpc.net/problem/3034


n, w, h = map(int, input().split())
for i in range(n):
    b = int(input())
    l = (w ** 2 + h ** 2) ** 0.5
    if b <= l:
        print("DA")
    else:
        print("NE")
