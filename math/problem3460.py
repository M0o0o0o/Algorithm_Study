# https://www.acmicpc.net/problem/3460

for _ in range(int(input())):
    num = list(bin(int(input())))[::-1]

    for i in range(len(num)):
        if num[i] == '1':
            print(i, end=' ')
