# https://www.acmicpc.net/problem/17608

n = int(input())
lst = [int(input()) for _ in range(n)][::-1]
big, ans = lst[0], 1

for i in range(1, n):
    if big < lst[i]:
        ans += 1
        big = lst[i]
        continue

print(ans)
