# # https://www.acmicpc.net/problem/1244


def tico(lst, num):
    start = num
    while start < n:
        lst[start] = 0 if lst[start] == 1 else 1
        start += num


def tica(lst, num):
    l, r = num - 1, num + 1
    lst[num] = 0 if lst[num] == 1 else 1
    while True:
        if 1 <= l and r < n:
            if lst[l] != lst[r]:
                break
            lst[r] = 0 if lst[r] == 1 else 1
            lst[l] = 0 if lst[l] == 1 else 1
            l -= 1
            r += 1
            continue
        break


n = int(input())
n += 1
lst = [0] + list(map(int, input().split()))
for _ in range(int(input())):
    gen, num = map(int, input().split())
    if gen == 1:
        tico(lst, num)
        continue
    tica(lst, num)

for i in range(1, n):
    print(lst[i], end=' ')
    if i % 20 == 0:
        print()
