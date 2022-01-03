# https://www.acmicpc.net/problem/12605

for i in range(1, int(input()) + 1) :
    lst = list(input().split(' '))[::-1]
    print('Case #' + str(i) + ":", end =' ')
    for l in lst : print(l, end = ' ')
    print()
    