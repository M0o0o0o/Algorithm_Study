# https://www.acmicpc.net/problem/2495

for _ in range(3):
    num = input() + '.'
    ans, count = 1, 1
    for i in range(1, len(num)):
        if num[i-1] == num[i]:
            count += 1
            continue
        ans = max(ans, count)
        count = 1

    print(ans)
