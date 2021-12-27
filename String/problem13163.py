# https://www.acmicpc.net/problem/13163

for _ in range(int(input())) :
    lst = list(input().split(' '))
    print('god', end = '')
    for i in range(1, len(lst)) :
        print(lst[i], end = '')
    print()