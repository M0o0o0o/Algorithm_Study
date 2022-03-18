# https://www.acmicpc.net/problem/2566

ans = -1

for i in range(9):
    lst = list(map(int, input().split()))
    for j in range(9):
        if lst[j] > ans:
            ans = lst[j]
            r, c = i + 1, j+1

print(ans)
print(r, c)
