# https://www.acmicpc.net/problem/4072


while True:
    string = input().strip('\n')
    if string == '#':
        break

    lst = string.split(' ')
    for s in lst:
        print(s[::-1], end=' ')
    print()
