# https://www.acmicpc.net/problem/11648

lst = list(input())
lst = list(map(int, lst))
ans = 0

while len(lst) >= 2:
    ans += 1
    mul = 1
    for l in lst:
        mul *= l

    lst = list(map(int, str(mul)))

print(ans)
