# https://www.acmicpc.net/problem/5355

for _ in range(int(input())):
    lst = list(input().split(' '))
    num = float(lst[0]) + 0.00
    for op in lst[1:]:
        if op == '@':
            num *= 3
        elif op == '%':
            num += 5
        else:
            num -= 7
    print("{:.2f}".format(num))
