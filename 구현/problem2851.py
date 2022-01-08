# https://www.acmicpc.net/problem/2851

ans = 0
mush = [int(input()) for _ in range(10)]
for m in mush :
    if abs(ans - 100) >= abs(ans + m - 100) :
        ans += m
        continue
    break

print(ans)