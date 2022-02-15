# https://www.acmicpc.net/problem/2145

while True:
    num = input()
    if num == '0':
        break
    lst = list(num)
    while len(lst) != 1:
        lst = list(str(sum(list(map(int, lst)))))
    print(lst[0])
